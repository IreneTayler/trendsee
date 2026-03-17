import asyncio
import logging

from fastapi import FastAPI

from .api import users, posts
from .db import Base, engine

logger = logging.getLogger(__name__)
app = FastAPI(title="Trendsee Feed Service")

STARTUP_DB_RETRIES = 30
STARTUP_DB_DELAY_SEC = 1


@app.on_event("startup")
async def on_startup() -> None:
    for attempt in range(1, STARTUP_DB_RETRIES + 1):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logger.info("Database ready, tables created.")
            return
        except Exception as e:
            if "starting up" in str(e).lower() or "connection" in str(e).lower():
                logger.warning("Database not ready (attempt %s/%s), retrying in %ss...", attempt, STARTUP_DB_RETRIES, STARTUP_DB_DELAY_SEC)
                await asyncio.sleep(STARTUP_DB_DELAY_SEC)
            else:
                raise
    raise RuntimeError("Database did not become ready in time.")


app.include_router(users.router, prefix="/api")
app.include_router(posts.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}

