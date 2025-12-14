from pydantic import BaseModel, Field

class TransactionRequest(BaseModel):
    transaction_id: str = Field(example="txn_1001")
    user_id: str = Field(example="user_123")
    amount: float = Field(example=2500.75)
    currency: str = Field(example="INR")
    merchant: str = Field(example="Amazon")

class TransactionResponse(BaseModel):
    transaction_id: str
    status: str
    risk_score: float
    message: str
