from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import VECTOR
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    description = Column(String)
    amount = Column(Float)
    category = Column(String)
    type = Column(String)
    embedding = Column(VECTOR(1536))
