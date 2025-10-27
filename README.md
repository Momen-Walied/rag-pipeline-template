# 🧠 RAG Pipeline Technical Challenge

[![GitHub Classroom](https://img.shields.io/badge/GitHub-Classroom-green.svg)](https://classroom.github.com)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00a393.svg)](https://fastapi.tiangolo.com)
[![Tests](https://img.shields.io/badge/tests-pytest-orange.svg)](https://pytest.org)

> **Technical Screening Assignment** | Estimated Time: 3-5 hours | Difficulty: Intermediate-Advanced

---

## 📖 Overview

Welcome to the **RAG Pipeline Challenge**! This assignment evaluates your ability to build production-ready AI systems using modern ML engineering practices.

You'll implement a **Retrieval-Augmented Generation (RAG)** system that can intelligently answer questions from research documents by combining document retrieval with large language models.

### 🎯 What You'll Build

A FastAPI-based service that:
- 📄 Extracts and processes text from PDF documents
- 🔍 Creates semantic embeddings and vector search capabilities
- 🤖 Retrieves relevant context and generates accurate answers using LLMs
- ⚡ Provides stable, well-tested REST API endpoints

---

## 🏗️ Architecture Requirements

### Core Components

```
┌─────────────────────────────────────────────────────┐
│                   FastAPI Service                   │
├─────────────────────────────────────────────────────┤
│  GET  /health    →  Health check endpoint           │
│  POST /ask       →  Question answering endpoint     │
└─────────────────────────────────────────────────────┘
                          ↓
         ┌────────────────┴────────────────┐
         ↓                                 ↓
┌──────────────────┐              ┌───────────────────┐
│  Vector Store    │              │   LLM Provider    │
│  (Qdrant/FAISS/  │              │     (Ollama)      │
│   ChromaDB)      │              │  Local Models <=1B│
└──────────────────┘              └───────────────────┘
```

### Required Stack

- **Framework**: FastAPI
- **Vector Database**: Qdrant, FAISS, or ChromaDB
- **Embeddings**: HuggingFace, Sentence Transformers, or local models
- **LLM**: **Ollama** (local models: Llama, Mistral, Phi, etc.) - **NO external APIs required**
- **Testing**: pytest with comprehensive test coverage

> **Important**: This challenge uses **Ollama for local LLM inference**. You do NOT need OpenAI, Anthropic, or any paid API keys.

---

## 📋 Functional Requirements

### 1️⃣ Document Processing
- Extract text from PDF files in the `/data` directory
- Handle multi-page documents efficiently
- Implement proper text chunking for semantic search
- Preserve document structure and context

### 2️⃣ Embedding & Indexing
- Generate embeddings for document chunks
- Build a searchable vector index
- Implement efficient similarity search
- Support incremental index updates

### 3️⃣ API Endpoints

#### `GET /health`
**Purpose**: Service health check for monitoring and orchestration

**Response**:
```json
{
  "status": "ok"
}
```

**Requirements**:
- Return 200 status code
- Respond within 100ms
- Always available (no external dependencies)

#### `POST /ask`
**Purpose**: Answer questions using RAG pipeline

**Request Body**:
```json
{
  "question": "What is retrieval-augmented generation?"
}
```

**Response**:
```json
{
  "answer": "Retrieval-augmented generation is...",
  "sources": ["document1.pdf", "document2.pdf"],  // Optional
  "confidence": 0.92  // Optional
}
```

**Requirements**:
- Accept JSON with `question` field
- Return JSON with `answer` field (required)
- Include relevant sources (bonus)
- Handle errors gracefully
- Response time < 5 seconds

### 4️⃣ Code Quality
- Clean, readable, well-documented code
- Proper error handling and logging
- Environment variable management for API keys
- Type hints and docstrings
- Follow PEP 8 style guidelines

---

## 🎓 Evaluation Criteria

### Automated Testing (10 points)

Your submission will be automatically graded via GitHub Classroom:

| Test | Points | Description |
|------|--------|-------------|
| **Health Endpoint** | 3 | `/health` returns correct response |
| **Ask Endpoint** | 7 | `/ask` accepts questions and returns answers |

### Manual Review (Additional Evaluation)

Reviewers will assess:

- **Architecture** (25%)
  - System design and component organization
  - Technology choices and justification
  - Scalability considerations

- **Code Quality** (25%)
  - Clean code principles
  - Documentation and comments
  - Error handling
  - Type safety

- **RAG Implementation** (30%)
  - Retrieval accuracy
  - Context relevance
  - Answer quality
  - Prompt engineering

- **Testing & Reliability** (20%)
  - Test coverage
  - Edge case handling
  - Error scenarios
  - Logging and monitoring

---

## 🚀 Getting Started

### Prerequisites

```bash
# Required
Python 3.10+
pip or conda
Ollama (for local LLM inference)

# Recommended
8GB+ RAM
GPU with CUDA support (optional, improves speed)
```

#### Install Ollama

**Linux/macOS**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows**:
Download from [ollama.com/download](https://ollama.com/download)

**Pull a model** (e.g., Llama 3 or Mistral):
```bash
ollama pull llama3
# or
ollama pull mistral
```

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ATS-score
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   ```bash
   # Create .env file (if needed for configuration)
   cp .env.example .env
   
   # Configure Ollama settings (optional)
   OLLAMA_HOST=http://localhost:11434
   OLLAMA_MODEL=llama3  # or mistral, phi, etc.
   ```
   
   > **Note**: No API keys required! Ollama runs locally.

4. **Prepare data**
   ```bash
   # Add your PDF files to /data directory
   mkdir -p data
   # Place research PDFs in data/
   ```

### Running Locally

```bash
# Start the API server
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

### Testing Your Implementation

```bash
# Run all tests
pytest tests/

# Run specific test
pytest tests/test_endpoints.py::test_health

# Run with coverage
pytest --cov=app --cov=src tests/
```

### Quick API Test

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test ask endpoint
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is RAG?"}'
```

---

## 📁 Project Structure

```
ATS-score/
├── app/
│   └── api.py              # FastAPI application and endpoints
├── src/
│   ├── main.py             # Main entry point
│   ├── rag_pipeline.py     # RAG implementation
│   └── utils.py            # Helper functions
├── tests/
│   └── test_endpoints.py   # Automated tests
├── data/                   # PDF documents (add your files here)
├── .github/
│   ├── classroom/
│   │   └── autograding.json  # Autograding configuration
│   └── workflows/
│       ├── classroom.yml     # GitHub Classroom workflow
│       └── test.yml          # CI/CD pipeline
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

---

## 💡 Implementation Tips

### Document Processing
```python
# Use efficient PDF parsing
from PyPDF2 import PdfReader

# Implement smart chunking
# - Semantic chunking (paragraphs, sections)
# - Overlap between chunks for context
# - Optimal chunk size: 500-1000 tokens
```

### Vector Store Setup
```python
# ChromaDB (easiest to start)
import chromadb
client = chromadb.Client()

# FAISS (fastest for production)
import faiss
index = faiss.IndexFlatL2(dimension)

# Qdrant (most feature-rich)
from qdrant_client import QdrantClient
client = QdrantClient(":memory:")
```

### RAG Pipeline Best Practices
1. **Retrieval**: Get top 3-5 most relevant chunks
2. **Reranking**: Optional - rerank by relevance
3. **Context Window**: Manage token limits (4k-32k depending on Ollama model)
4. **Prompt Engineering**: Clear instructions + context + question
5. **Fallbacks**: Handle no relevant context found

### Ollama Integration
```python
# Simple Ollama API call
import requests

response = requests.post('http://localhost:11434/api/generate',
    json={
        'model': 'llama3',
        'prompt': 'Your prompt with context',
        'stream': False
    })

# Or use langchain with Ollama
from langchain.llms import Ollama
llm = Ollama(model="llama3")
answer = llm(prompt)
```

### Error Handling
```python
# Always validate inputs
# Handle API rate limits
# Graceful degradation
# Meaningful error messages
```

---

## 🎁 Bonus Features (Optional)

 Impress us with:

- 📊 **Streaming responses** using Server-Sent Events
- 🔄 **Caching** for repeated questions
- 📈 **Metrics & monitoring** (Prometheus, Grafana)
- 🧪 **Evaluation metrics** (retrieval accuracy, answer relevance)
- 🚀 **Deployment** to Hugging Face Spaces, Railway, or Render
- 🐳 **Docker** containerization
- 📝 **API documentation** with Swagger/OpenAPI
- 🔐 **Authentication** (API keys, JWT)
- ⚡ **Async processing** for better performance
- 🌍 **Multi-language support**

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError`
```bash
# Solution: Ensure all dependencies are installed
pip install -r requirements.txt --upgrade
```

**Issue**: Ollama not running
```bash
# Solution: Start Ollama service
ollama serve
# Or check if Ollama is running
curl http://localhost:11434/api/tags
```

**Issue**: Tests failing
```bash
# Solution: Ensure Ollama is running before tests
# Check that your API doesn't require Ollama for health check
# Mock Ollama calls in unit tests if needed
```

**Issue**: Out of memory
```bash
# Solution: Use smaller embedding models or implement batching
# Consider using quantized models
```

---

## 📚 Resources

### Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [LangChain Ollama Integration](https://python.langchain.com/docs/integrations/llms/ollama)
- [Qdrant Documentation](https://qdrant.tech/documentation/)

### Learning Materials
- [RAG Explained](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- [Vector Databases Guide](https://www.pinecone.io/learn/vector-database/)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

## ⏱️ Time Management

Recommended time allocation:

- **Setup & Research** (30 min): Environment setup, architecture planning
- **Document Processing** (1 hour): PDF parsing, text extraction
- **Vector Store** (1 hour): Embeddings, indexing, search
- **RAG Pipeline** (1.5 hours): LLM integration, prompt engineering
- **API Development** (45 min): FastAPI endpoints, validation
- **Testing & Debugging** (45 min): Write tests, fix issues
- **Documentation** (30 min): Code comments, README updates

**Total**: ~5-6 hours (can be completed faster with experience)

---

## 📝 Submission Guidelines

1. ✅ Ensure all tests pass: `pytest tests/`
2. ✅ Ensure Ollama models are documented (which model you used)
3. ✅ Commit all changes to your repository
4. ✅ Push to GitHub (autograding runs automatically)
5. ✅ Verify GitHub Actions workflow succeeds
6. ✅ Include a brief architecture explanation in comments

### What to Include

- ✅ All source code
- ✅ Updated `requirements.txt`
- ✅ `.env.example` with Ollama configuration (if used)
- ✅ Test files
- ✅ Documentation of which Ollama model you used (e.g., llama3, mistral)

### What NOT to Include

- ❌ Downloaded Ollama models (candidates will pull their own)
- ❌ Large model files or embeddings
- ❌ Virtual environment folders
- ❌ `__pycache__` or `.pyc` files
- ❌ Large data files (provide download links instead)

---

## 🤝 Support

If you encounter issues:

1. Check the **Troubleshooting** section above
2. Review GitHub Actions logs for test failures
3. Consult the provided documentation links
4. For clarifications, open an issue in the repository

---

## 📄 License

This challenge is provided for educational and evaluation purposes.

---

## 🌟 Good Luck!

We're excited to see your implementation! Focus on:
- ✨ Clean, readable code
- 🎯 Working functionality
- 🧪 Proper testing
- 📖 Clear documentation

**Remember**: A simple, working solution is better than a complex, broken one. Start with the basics and iterate!

---

*Last Updated: 2025-10-27*
