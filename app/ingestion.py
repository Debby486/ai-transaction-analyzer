import pandas as pd
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Transaction
from app.llm import embed_text


def load_transactions_csv(csv_path: str):
    """
    Loads a CSV file containing transactions into a pandas DataFrame.
    Expected columns: date, description, amount, category, type
    """
    df = pd.read_csv(csv_path)
    return df


def ingest_transactions(csv_path: str):
    """
    Loads CSV, generates embeddings, and inserts into the database.
    """
    df = load_transactions_csv(csv_path)
    db: Session = SessionLocal()

    for _, row in df.iterrows():
        text = f"{row['date']} {row['description']} {row['amount']} {row['category']} {row['type']}"
        embedding = embed_text(text)

        transaction = Transaction(
            date=row["date"],
            description=row["description"],
            amount=float(row["amount"]),
            category=row["category"],
            type=row["type"],
            embedding=embedding,  # list[float] -> PGVector
        )

        db.add(transaction)

    db.commit()
    db.close()

    print("✓ Finished ingesting transactions")


if __name__ == "__main__":
    ingest_transactions("data/transactions.csv")
