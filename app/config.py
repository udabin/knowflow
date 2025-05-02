from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    embedding_model: str = "snunlp/KR-SBERT-V40K-klueNLI-augSTS"
    vectorstore_path: str = "./data/vectorstore/index.faiss"
    project_name: str = "KnowFlow"

    class Config:
        env_file = ".env"

# 전역 설정 객체
settings = Settings()