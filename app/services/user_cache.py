import json
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

async def get_user_profile(user_id: str):
    key = f"user_profile:{user_id}"

    cached = redis_client.get(key)
    if cached:
        print("CACHE HIT")
        return json.loads(cached)

    print("CACHE MISS")

    # Simulated DB call
    user_data = {
        "user_id": user_id,
        "balance": 10000,
        "home_country": "IN"
    }

    redis_client.setex(key, 60, json.dumps(user_data))
    return user_data
