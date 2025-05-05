# KnowFlow

> Internal Knowledge Assistant powered by RAG + LangChain  
> Upload documents, ask natural language questions, and get contextual answers instantly.


## Overview

**KnowFlow** is a Retrieval-Augmented Generation (RAG) system that provides contextual answers to user queries based on internal documents.  
It uses FastAPI as the backend, vectorizes documents into a FAISS index, and routes tasks to appropriate agents using multi-agent logic.


## Tech Stack

- **FastAPI** – Web API server  
- **LangChain** – Chain and document retrieval logic  
- **FAISS** – Local vector database  
- **OpenAI GPT-3.5 / GPT-4** – Answer generation  
- **HuggingFace Embedding** – `snunlp/KR-SBERT-V40K-klueNLI-augSTS`  
- **Sentence Transformers** – Used for multi-prompt embedding similarity-based routing  
- **Pydantic + pydantic-settings** – Configuration management  
- **Uvicorn** – ASGI server  
- **Streamlit** – Lightweight UI demo


## File Descriptions  
- `main.py` – FastAPI application entry point  
- `config.py` – Loads environment variables  
- `router.py` – Multi-agent routing logic  
- `agents/` – Includes `SummaryAgent`, `QAAgent`, `NERAgent`, `ClassificationAgent`, and `FallbackAgent`  
- `retriever.py` – FAISS-based document retriever  
- `generator.py` – GPT-based response generator  
- `ingestion.py` – Loads, splits, embeds documents and saves vectorstore  
- `streamlit_app.py` – Streamlit-based UI demo  
- `utils.py` – Utility functions (stub)  
- `agent.py` – Agent interface definition (stub)  
- `data/docs/` – Directory for raw text and PDF files  
- `data/vectorstore/` – FAISS vector index storage


## Features

- RAG-based response generation  
- Named entity extraction, classification, summarization  
- REST API endpoint (`/ask`)  
- Full Korean embedding support  


## Usage

### 1. Set up `.env`
```bash
OPENAI_API_KEY=your-openai-key
EMBEDDING_MODEL=snunlp/KR-SBERT-V40K-klueNLI-augSTS 
VECTORSTORE_PATH=./data/vectorstore/index.faiss
```

### 2. Install dependencies
```bash
pip install -r app/requirements.txt
```

### 3. Embed documents
```bash
PYTHONPATH=. python core/ingestion.py
```

### 4. Run the API server
```bash
uvicorn app.main:app --reload
→ 브라우저에서 http://localhost:8000/docs 접속
```

### 5. Launch the Streamlit UI
```bash
streamlit run interface/streamlit_app.py
```

## TODO
- Enhance multi-agent routing with LangGraph or FSM
- Upload API for new documents
- Automatic report generation (PDF/Markdown)
- Save chat history per user
- Support for local LLMs (e.g., Ollama, GPT4All)

## License
MIT License © 2025 KnowFlow

 
