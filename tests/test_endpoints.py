from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_ask():
    res = client.post("/ask", json={"question": "What is RAG?"})
    assert res.status_code == 200
    assert "answer" in res.json()
