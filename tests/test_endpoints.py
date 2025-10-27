from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

# Import the FastAPI app - this will fail if not implemented correctly
from app.api import app

client = TestClient(app)

def test_health():
    """Test health endpoint - no external dependencies"""
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

@patch('requests.post')  # Mock Ollama API calls
def test_ask(mock_post):
    """Test ask endpoint with mocked Ollama response"""
    # Mock Ollama response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "response": "RAG stands for Retrieval-Augmented Generation..."
    }
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    
    # Test the endpoint
    res = client.post("/ask", json={"question": "What is RAG?"})
    assert res.status_code == 200
    assert "answer" in res.json()
    assert len(res.json()["answer"]) > 0
