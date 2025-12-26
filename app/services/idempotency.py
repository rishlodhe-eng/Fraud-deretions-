import json
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

IDEMPOTENCY_TTL = 300  # 5 minutes

def check_idempotency(key: str):
    cached = redis_client.get(key)
    if cached:
        return json.loads(cached)
    return None

def save_idempotency(key: str, response: dict):
    redis_client.setex(key, IDEMPOTENCY_TTL, json.dumps(response))
