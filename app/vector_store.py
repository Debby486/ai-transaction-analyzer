from typing import List
from sqlalchemy import select

from app.database import SessionLocal
from app.models import Transaction as TransactionORM
from app.llm import embed_text
from app.schemas import Transaction as TransactionSchema


def search_similar_transactions(query: str, top_k: int = 5) -> List[TransactionSchema]:
    """
    Embed the query, then use PGVector to find the most similar transactions.
    """
    query_embedding = embed_text(query)

    with SessionLocal() as db:
        stmt = (
            select(TransactionORM)
            .order_by(TransactionORM.embedding.cosine_distance(query_embedding))
            .limit(top_k)
        )
        results = db.execute(stmt).scalars().all()

        # convert ORM objects -> Pydantic models
        return [TransactionSchema.model_validate(tx) for tx in results]
