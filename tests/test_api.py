from fastapi.testclient import TestClient
from banking_lab.api import app, _seen

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_submit_and_idempotency():
    _seen.clear()
    body = {"inquiry_id": "SYN-100", "question": "Find policy procedure"}
    a = client.post("/inquiries", json=body, headers={"Idempotency-Key": "test-key"})
    b = client.post("/inquiries", json=body, headers={"Idempotency-Key": "test-key"})
    assert a.status_code == 200 and a.json() == b.json()
    assert a.headers["X-Request-ID"]
    conflict = client.post("/inquiries", json={**body, "question": "Something different"}, headers={"Idempotency-Key": "test-key"})
    assert conflict.status_code == 409

def test_invalid_payload():
    assert client.post("/inquiries", json={"inquiry_id": "x", "question": ""}).status_code == 422
