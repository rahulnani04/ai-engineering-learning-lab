# Lab 01 — Python and FastAPI: explain what you built

## Problem
An analyst submits a *synthetic* inquiry. The service must validate the request, classify it, and return a predictable result. Repeated submissions with the same idempotency key should not produce conflicting results.

## What / why / how
| Concept | What it is | Why it matters here | Find it |
|---|---|---|---|
| Function | Reusable operation | Isolate route logic | `InquiryService.classify` |
| Class | Bundles behavior | Separate HTTP from domain rules | `InquiryService` |
| Type hint | Static contract | Clarify expected parameters | `classify(question: str) -> Category` |
| Pydantic | Runtime data validation | Reject malformed requests | `Inquiry` |
| Decorator | Registration/wrapping mechanism | Register HTTP route | `@app.post` |
| Dependency injection | Provide dependencies externally | Swap service in tests | `Depends(get_service)` |
| Async endpoint | Coroutine request handler | Supports async I/O integrations | `create_inquiry` |
| Middleware | Cross-cutting request processing | Add request correlation ID | `add_request_id` |
| Exception handler | Maps errors to HTTP responses | Avoid raw internal errors | `runtime_error_handler` |
| Logging | Operational records | Understand request outcome | `logger.info` |
| Unit test | Test isolated behavior | Detect classification regression | `test_domain.py` |
| API test | Test HTTP behavior | Verify validation and duplicate keys | `test_api.py` |
| Idempotency | Safe repeated effect | Detect duplicate conflicting request | `Idempotency-Key` |
| AsyncIO | Cooperative concurrency for I/O | Overlap independent awaits | `concurrency_demo.py` |

## Architecture
`HTTP request → Pydantic → FastAPI route → injected InquiryService → deterministic result`.

## What this does NOT prove
There is no actual authentication, RAG, database, LLM, distributed idempotency, circuit breaker, or live service. `_seen` is in-memory and not safe across workers, restarts or simultaneous races. Replace with a durable atomic store in a later lab.

## Exercises
1. Add a `GET /inquiries/{id}` lookup using a repository abstraction and tests.
2. Implement explicit `401`/`403` paths using **synthetic** identities. Do not call this production-grade JWT auth until signatures/claims are validated.
3. Add a deadline and bounded retry around a simulated flaky dependency; explain which errors are retryable.
4. Add a fake database session context manager and prove cleanup on exceptions.
5. Add an asynchronous generator and SSE endpoint; test that it finishes and handles cancellation.
6. Implement an injectable cache with a TTL and explain stale reads.
7. Run the concurrency demo, then replace async sleeps with blocking sleeps to observe what changes.
8. Explain when threads or processes would be preferable.

## Interview rehearsal
> "I built a synthetic banking inquiry API as a personal learning project. It validates input with Pydantic, isolates business logic in a service class, uses FastAPI dependency injection and request logging, and tests invalid and repeated submissions. I also compared sequential and concurrent simulated I/O. The project intentionally doesn't claim to reproduce my employer's proprietary architecture."

## Design review prompts
- Why is `idempotency_key` a request header?
- How does a 422 differ from a 409?
- Why is a shared in-memory dictionary unsuitable for distributed production services?
- Does marking a route `async` make `service.process` asynchronous?
- What changes when a workflow performs real database or model network calls?
