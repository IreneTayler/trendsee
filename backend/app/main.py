from fastapi import FastAPI

from .api import users, posts
from .db import Base, engine


app = FastAPI(title="Trendsee Feed Service")


@app.on_event("startup")
async def on_startup() -> None:
    # Простейшее создание таблиц (для тестового можно без Alembic)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(users.router, prefix="/api")
app.include_router(posts.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}

