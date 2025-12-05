from pydantic import BaseModel, ConfigDict
from typing import List


class Transaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date: str
    description: str
    amount: float
    category: str
    type: str


class AskRequest(BaseModel):
    query: str


class AskResponse(BaseModel):
    query: str
    answer: str
    retrieved_transactions: List[Transaction]
