# 1. 문서 수집
# 2. 문단 분할 (chunk)
# 3. 임베딩 생성
# 4. vector db에 저장

import os
from pathlib import Path
from typing import List

from langchain.documet_loaders import DirectoryLoader, TextLoader, UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.config import settings

def load_documents(directory: str) ->  List:
    """docs 폴더 내 문서 불러오기"""
    loaders = [
        DirectoryLoader(directory, glob="**/*.txt", loader_cls=TextLoader),
        DirectoryLoader(directory, glob="**/*.pdf", loader_cls=UnstructuredPDFLoader),
    ]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    return docs

def split_documents(docs: List, chunk_size: int = 500, chunk_overlap: int = 100) -> List:
    """문서 조각으로 분할"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def embed_and_store(chunks: List, persist_path: str):
    """임베딩 후 FAISS 벡터스토어에 저장"""
    embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    vectorstore.save_local(persist_path)

def ingest_documents():
    print("문서 인덱싱 시작...")
    docs = load_documents("./data/docs")
    print(f"문서 수: {len(docs)}")

    chunks = split_documents(docs)
    print(f"분할된 청크 수: {len(chunks)}")

    embed_and_store(chunks, settings.vectorstore_path)
    print("벡터스토어 저장 완료!")