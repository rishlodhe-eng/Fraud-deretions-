from fastapi import FastAPI, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis
from fastapi import Header, HTTPException
from app.services.idempotency import check_idempotency, save_idempotency


from app.services.user_cache import get_user_profile

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis_client = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )
    await FastAPILimiter.init(redis_client)

@app.get("/")
async def root():
    return {"status": "SentinelStream running"}

@app.post("/transaction")
async def transaction(
    user_id: str,
    idempotency_key: str = Header(...)
):
    cached = check_idempotency(idempotency_key)
    if cached:
        return cached

    user = await get_user_profile(user_id)

    response = {
        "status": "processed",
        "user": user
    }

    save_idempotency(idempotency_key, response)
    return response

