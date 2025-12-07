from sqlalchemy import Column, Integer, String, Float
from pgvector.sqlalchemy import Vector
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    description = Column(String)
    amount = Column(Float)
    category = Column(String)
    type = Column(String)
    embedding = Column(Vector(dim=384))
