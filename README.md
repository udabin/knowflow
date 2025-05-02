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


## Project Structure
knowflow/
├── app/
│   ├── main.py            # FastAPI 엔드포인트
│   ├── config.py          # .env 설정 로딩
│   ├── requirements.txt   # 패키지 목록
│   └── .env               # API 키 등 민감 정보
│
├── core/
│   ├── ingestion.py       # 문서 로딩, 임베딩, 저장
│   ├── retriever.py       # 질문에 맞는 문서 검색
│   ├── generator.py       # LLM 기반 답변 생성
│   └── utils.py           # 공통 유틸 함수 (예정)
│
├── data/
│   ├── docs/              # 원본 문서들 (.txt, .pdf 등)
│   └── vectorstore/       # FAISS 인덱스 저장 경로


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

 
