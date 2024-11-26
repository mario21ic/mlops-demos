from fastapi import FastAPI
import modelo

app = FastAPI()

@app.get("/")
def root():
    return {"ok": 1}

@app.get("/analyze")
def analyze(q: str):
    return modelo.analiza(q)

