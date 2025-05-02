# 1. 사용자 질문
# 2. 벡터 변환
# 3. 벡터 DB(FAISS)에서 가장 유사한 문서 검색

# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from typing import List

from app.config import settings

def load_vectorstore(persist_path: str) -> FAISS:
    """저장된 FAISS 인덱스를 불러온다"""
    embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    return FAISS.load_local(persist_path, embeddings)

def retrieve_documents(query: str, top_k: int = 3) -> list[Document]:
    """질문과 유사한 문서를 벡터 DB에서 검색"""
    vectorstore = load_vectorstore(settings.vectorstore_path)
    results = vectorstore.similarity_search(query, k=top_k)
    return results