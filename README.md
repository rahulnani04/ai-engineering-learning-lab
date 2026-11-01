# AI Engineering Learning Lab

A **hands-on learning portfolio**, not a representation of proprietary Fifth Third Bank/HCA systems. Every example uses synthetic data and should be described as an independent learning project.

## The method
For each topic: (1) problem statement, (2) concepts, (3) architecture, (4) implement, (5) tests and failure cases, (6) technical trade-offs, (7) explanation in your own words, (8) publish with a README.

## First runnable project: Banking Inquiry API
A synthetic banking operations API that validates questions, selects an inquiry category and produces safe mock results. It illustrates Python functions/classes, type hints, decorators (FastAPI), context managers (tests), async endpoints, dependency injection, HTTP errors, middleware, logging, unit tests and idempotency. **No real bank data, model calls or external credentials.**

### Quick start
```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\\Scripts\\activate
pip install -e '.[dev]'
uvicorn banking_lab.api:app --reload
```

Open `http://127.0.0.1:8000/docs` and try `POST /inquiries` with:
```json
{"inquiry_id":"SYN-1001","question":"Find the policy for a transaction alert"}
```
Run `pytest -q`. `python -m banking_lab.concurrency_demo` demonstrates sequential vs concurrent I/O. All response bodies are synthetic.

## Repository layout
- `src/banking_lab/domain.py`: typed models, classes, business rules
- `src/banking_lab/api.py`: FastAPI, dependency injection, request IDs, error handling and idempotency
- `src/banking_lab/concurrency_demo.py`: `asyncio` example with artificial I/O
- `tests/`: unit and API tests
- `docs/`: explanations, exercises, interview walkthroughs, roadmap

## Public GitHub safety
Do not add client code, real internal policy text, PHI, PII, secrets, genuine client records, internal architecture diagrams or screenshots. Use synthetic company names and data. Don't portray this lab as employer-delivered work.
