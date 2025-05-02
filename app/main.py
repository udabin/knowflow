from fastapi import FastAPI, Request
from pydantic import BaseModel
from core.generator import generate_answer

app = FastAPI(title="KnowFlow - Internal Knowledge Assistant")

class QueryRequest(BaseModel):
    query: str
    top_k: int=3

@app.post("/ask")
async def ask(request: QueryRequest):
    try:
        answer = generate_answer(request.query, top_k=request.top_k)
        return {
            "query": request.query,
            "answer": answer
        }
    except Exception as e:
        return {
            "error": str(e)
        }
    
@app.get("/")
def health_check():
    return {"status": "ok", "message": "KnowFlow is running"}