# KnowFlow

> Internal Knowledge Assistant powered by RAG + LangChain  
> Upload documents, ask natural language questions, and get contextual answers instantly.


## Overview

KnowFlow는 기업 내부 문서를 기반으로 자연어 질문에 대한 정확한 응답을 생성하는 RAG 시스템입니다.  
FastAPI 서버를 기반으로 동작하며 문서를 벡터화하여 FAISS DB에 저장하고 OpenAI GPT 모델을 활용해 답변을 생성합니다.


## Tech Stack

- **FastAPI** - Web API 서버
- **LangChain** - 체인 구성 및 벡터 검색 처리
- **FAISS** - 로컬 벡터 데이터베이스
- **OpenAI GPT-4** - 답변 생성
- **HuggingFace Embedding** - `snunlp/KR-SBERT-V40K-klueNLI-augSTS`
- **Pydantic + pydantic-settings** - 설정 관리
- **Uvicorn** - ASGI 서버 실행


## File Descriptions
- main.py – FastAPI entry point (API server)
- config.py – Loads settings from .env
- requirements.txt – Project dependency list
- .env – API keys and other sensitive information
- ingestion.py – Loads, splits, and embeds documents
- retriever.py – Searches for documents similar to the query
- generator.py – Generates answers using GPT
- utils.py – Utility functions (planned)
- docs/ – Original documents (e.g., .txt, .pdf)
- vectorstore/ – FAISS index storage path


## Features

- [x] 문서 업로드 및 벡터화
- [x] 유사 문서 검색 (FAISS)
- [x] GPT 기반 답변 생성 (RAG)
- [x] REST API 제공 (`/ask`)
- [x] 한글 임베딩 모델 지원


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

### 3. Ingest documents
```bash
python3 -m core.ingestion
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
→ 브라우저에서 http://localhost:8000/docs 접속
```

## TODO
- Multi-agent extension (LangGraph or FSM)
- Upload API for documents
- PDF or Markdown report generation
- Chat history storage

## License
MIT License © 2025 KnowFlow

 
