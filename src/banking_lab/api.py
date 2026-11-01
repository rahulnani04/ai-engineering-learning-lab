"""FastAPI practice app. No real bank information, identity or LLM involved."""
import logging
import uuid
from collections.abc import Callable
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from .domain import Inquiry, InquiryResult, InquiryService

logger = logging.getLogger("banking_lab")
app = FastAPI(title="Synthetic Banking Inquiry Lab", version="0.1.0")
_service = InquiryService()
_seen: dict[str, tuple[Inquiry, InquiryResult]] = {}  # Single-process demo only, not production persistence.

def get_service() -> InquiryService:
    return _service

@app.middleware("http")
async def add_request_id(request: Request, call_next: Callable):
    request_id = str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    logger.info("request method=%s path=%s status=%s request_id=%s",
                request.method, request.url.path, response.status_code, request_id)
    return response

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/inquiries", response_model=InquiryResult)
async def create_inquiry(
    inquiry: Inquiry,
    idempotency_key: str | None = Header(default=None, max_length=128),
    service: InquiryService = Depends(get_service),
):
    if idempotency_key and idempotency_key in _seen:
        old_input, old_result = _seen[idempotency_key]
        if old_input != inquiry:
            raise HTTPException(status_code=409, detail="Idempotency key reused with different input")
        return old_result
    result = service.process(inquiry)
    if idempotency_key:
        _seen[idempotency_key] = (inquiry, result)
    return result

@app.exception_handler(RuntimeError)
async def runtime_error_handler(request: Request, exc: RuntimeError):
    logger.error("runtime error on %s: %s", request.url.path, type(exc).__name__)
    return JSONResponse(status_code=503, content={"detail": "A dependency is unavailable"})
