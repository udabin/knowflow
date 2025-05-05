from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.agents.router import route_query
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
    
@app.post("/query")
async def handle_query(request: Request):
    body = await request.json()
    query = body.get("query")
    result = route_query(query)
    return {"response": result}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "KnowFlow is running"}