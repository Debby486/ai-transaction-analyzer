from typing import List
from sentence_transformers import SentenceTransformer
from app.schemas import Transaction as TransactionSchema

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list:
    """
    Generates a 384-dimensional embedding for the given text using a HuggingFace model.
    """
    embedding = model.encode(text)
    return embedding.tolist()

def answer_question_with_context(query: str, transactions: List[TransactionSchema]) -> str:
    """
    Provide a clean, focused answer based on only the most relevant transaction.
    """
    if not transactions:
        return f"I couldn’t find any transactions related to your query: \"{query}\"."

    # Pick only the most relevant (first in the similarity ranking)
    main = transactions[0]

    # Build clean summary
    lines = []
    lines.append(f"Here’s the closest match for your query: \"{query}\".\n")

    lines.append("**Transaction Details:**")
    lines.append(f"- **Description:** {main.description}")
    lines.append(f"- **Amount:** ₦{main.amount:,.2f}")
    lines.append(f"- **Type:** {main.type.capitalize()}")
    lines.append(f"- **Category:** {main.category}")
    lines.append(f"- **Date:** {main.date}")

    # Add a friendly summary sentence
    if main.type == "credit":
        lines.append(f"\nThis appears to be an income of **₦{main.amount:,.2f}**.")
    else:
        lines.append(f"\nThis appears to be a spending of **₦{main.amount:,.2f}**.")

    return "\n".join(lines)
