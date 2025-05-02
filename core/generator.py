# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from app.config import settings
from core.retriever import load_vectorstore

def generate_answer(query: str, top_k: int=3) -> str:
    """query를 입력받아 검색된 문서를 기반으로 답변 생성"""

    # 벡터 db 로드
    vectorstore = load_vectorstore(settings.vectorstore_path)

    # LLM
    llm = ChatOpenAI(
        model_name="gpt-4",
        temperature=0,
        openai_api_key=settings.openai_api_key
    )

    # RAG 체인 구성 : 검색 + 답변 생성
    qa_chain = RetreivalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": top_k}),
        return_source_documents=False
    )

    # 답변 생성
    response = qa_chain.run(query)
    return response