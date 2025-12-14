from fastapi import FastAPI, HTTPException
from schemas import TransactionRequest, TransactionResponse

app = FastAPI(
    title="Transaction Processing API",
    description="Swagger / OpenAPI documentation for Transaction API",
    version="1.0.0"
)

@app.post(
    "/transactions/validate",
    response_model=TransactionResponse,
    summary="Validate Transaction",
    description="""
    Validates a transaction request.

    - Accepts transaction details
    - Performs basic validation
    - Returns transaction status and risk score
    """,
    tags=["Transactions"],
    responses={
        200: {"description": "Transaction validated successfully"},
        400: {"description": "Invalid transaction data"},
        429: {"description": "Too many requests"},
        500: {"description": "Internal server error"}
    }
)
async def validate_transaction(txn: TransactionRequest):

    if txn.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    return {
        "transaction_id": txn.transaction_id,
        "status": "APPROVED",
        "risk_score": 0.15,
        "message": "Transaction processed successfully"
    }
