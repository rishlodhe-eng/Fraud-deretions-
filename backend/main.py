from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SentinelStream Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "SentinelStream Backend Running"}

@app.get("/api/kpis")
def get_kpis():
    return {
        "tps": 42120,
        "fraud_rate": "1.92%",
        "avg_latency": "137ms",
        "blocked_tx": 12431
    }

@app.get("/api/transactions")
def get_transactions():
    return [
        {
            "id": "TX1001",
            "user": "Alice",
            "amount": 1200,
            "risk": "Low",
            "status": "Approved"
        },
        {
            "id": "TX1002",
            "user": "Bob",
            "amount": 5600,
            "risk": "High",
            "status": "Blocked"
        }
    ]
