from fastapi import FastAPI

app = FastAPI(
    title="Sunny AI",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "company": "Sunny AI",
        "status": "online",
        "message": "Welcome to Sunny AI"
    }
