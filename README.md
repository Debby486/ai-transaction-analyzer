# AI Transaction Analyzer

FastAPI + PGVector + HuggingFace Local Embeddings

🧠 Overview

A semantic AI system that analyzes financial transactions using local embedding models and PGVector.

Users can ask questions like:

“How much did I spend on food?”

“How much, in total was spent on bank charges?”

“Airtime transactions in January?”

The system retrieves relevant transactions and generates a clean, human-friendly summary.

# Tech Stack

FastAPI

PostgreSQL + PGVector – vector similarity search

HuggingFace SentenceTransformers – local embeddings

Python 3.10

Uvicorn

SQLAlchemy

📂 Project Structure
app/
  ├── main.py
  ├── database.py
  ├── ingestion.py
  ├── llm.py
  ├── vector_store.py
  ├── models.py
  ├── schemas.py

⚙️ Setup
1. Clone repo
git clone https://github.com/Debby486/ai-transaction-analyzer.git
cd ai-transaction-analyzer

2. Create virtual environment

3. Ingest sample transactions
python -m app.ingestion

4. Run app
uvicorn app.main:app --reload

Example Query
POST /ask
{
  "query": “How much did I spend on food?”
}
