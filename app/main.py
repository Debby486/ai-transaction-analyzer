from fastapi import FastAPI

app = FastAPI(title="AI Transaction Analyzer")

@app.get("/")
def root():
    return {"message": "AI Transaction Analyzer is running"}
