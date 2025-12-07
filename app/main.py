from fastapi import FastAPI

from app.vector_store import search_similar_transactions
from app.schemas import AskRequest, AskResponse
from app.llm import answer_question_with_context

app = FastAPI(title="AI Transaction Analyzer")

@app.get("/")
def root():
    return {"message": "AI Transaction Analyzer is running"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest):
    # 1. semantic search over transactions
    hits = search_similar_transactions(payload.query, top_k=5)

    # 2. build a human-readable answer
    answer = answer_question_with_context(payload.query, hits)

    return AskResponse(
        query=payload.query,
        answer=answer,
        retrieved_transactions=hits,
    )
