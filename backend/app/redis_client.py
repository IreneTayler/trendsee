from typing import AsyncGenerator

import redis.asyncio as redis

from .core.config import get_settings


_redis: redis.Redis | None = None


def get_redis_client() -> redis.Redis:
    global _redis
    if _redis is None:
        settings = get_settings()
        url = settings.redis_url or "redis://redis:6379/0"
        _redis = redis.from_url(url, decode_responses=True)
    return _redis


async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    client = get_redis_client()
    yield client

