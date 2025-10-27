"""
FastAPI Application for RAG Pipeline

This is a minimal working implementation for testing the template.
Candidates should expand this with full RAG pipeline functionality.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="RAG Pipeline API")

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

@app.get("/health")
def health_check():
    """Health check endpoint - no external dependencies"""
    return {"status": "ok"}

@app.post("/ask", response_model=Answer)
def ask_question(question: Question):
    """
    Answer questions using RAG pipeline with Ollama.
    
    In a full implementation, this would:
    1. Retrieve relevant document chunks from vector store
    2. Build context with retrieved chunks
    3. Send to Ollama for answer generation
    """
    try:
        # Attempt to call Ollama (will be mocked in tests)
        ollama_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        response = requests.post(
            f"{ollama_url}/api/generate",
            json={
                "model": os.getenv("OLLAMA_MODEL", "llama3"),
                "prompt": f"Answer this question: {question.question}",
                "stream": False
            },
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            return {"answer": result.get("response", "No answer generated")}
    except Exception:
        # Graceful fallback if Ollama is not available
        pass
    
    # Fallback response for testing
    return {"answer": f"RAG pipeline response for: {question.question}"}
