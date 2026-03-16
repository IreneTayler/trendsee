import asyncio
from datetime import datetime, timedelta, timezone
from typing import Sequence

from redis.asyncio import Redis

from ..models import Post
from ..repositories.posts import PostRepository
from ..schemas import PostCreate, PostRead, PostUpdate


HOT_PERIOD_MINUTES = 10


def _post_cache_key(post_id: int) -> str:
    return f"post:{post_id}"


class PostService:
    def __init__(self, repo: PostRepository, redis: Redis):
        self.repo = repo
        self.redis = redis

    async def _serialize_post(self, post: Post) -> dict:
        return {
            "id": post.id,
            "user_id": post.user_id,
            "title": post.title,
            "text": post.text,
            "created_at": post.created_at.isoformat(),
            "updated_at": post.updated_at.isoformat(),
        }

    async def _deserialize_post(self, data: dict) -> PostRead:
        return PostRead(
            id=int(data["id"]),
            user_id=int(data["user_id"]),
            title=data["title"],
            text=data["text"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

    async def _is_hot(self, created_at: datetime) -> bool:
        now = datetime.now(timezone.utc)
        # created_at может быть naive, приведём
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=timezone.utc)
        return now - created_at <= timedelta(minutes=HOT_PERIOD_MINUTES)

    async def create_post(self, user_id: int, data: PostCreate) -> PostRead:
        post = await self.repo.create_post(user_id=user_id, title=data.title, text=data.text)
        serialized = await self._serialize_post(post)
        # Кладём в Redis с TTL в 10 минут (горячий период)
        await self.redis.hset(_post_cache_key(post.id), mapping=serialized)
        await self.redis.expire(_post_cache_key(post.id), HOT_PERIOD_MINUTES * 60)
        return PostRead.from_orm(post)

    async def update_post(self, post_id: int, data: PostUpdate) -> PostRead | None:
        post = await self.repo.get_post(post_id)
        if not post:
            return None

        updated = await self.repo.update_post(
            post_id,
            title=data.title if data.title is not None else None,
            text=data.text if data.text is not None else None,
        )
        if not updated:
            return None

        serialized = await self._serialize_post(updated)
        await self.redis.hset(_post_cache_key(updated.id), mapping=serialized)
        await self.redis.expire(_post_cache_key(updated.id), HOT_PERIOD_MINUTES * 60)
        return PostRead.from_orm(updated)

    async def delete_post(self, post_id: int) -> None:
        await self.repo.delete_post(post_id)
        await self.redis.delete(_post_cache_key(post_id))

    async def get_post(self, post_id: int) -> PostRead | None:
        # Пытаемся взять из Redis
        cache_key = _post_cache_key(post_id)
        cached = await self.redis.hgetall(cache_key)
        if cached and "created_at" in cached:
            # Считаем, что из Redis всегда "горячие" данные
            return await self._deserialize_post(cached)

        # Из БД (с задержкой 2 секунды)
        post = await self.repo.get_post(post_id)
        if not post:
            return None

        if await self._is_hot(post.created_at):
            # если пост ещё горячий, кладём в кэш
            serialized = await self._serialize_post(post)
            await self.redis.hset(cache_key, mapping=serialized)
            await self.redis.expire(cache_key, HOT_PERIOD_MINUTES * 60)
            return PostRead.from_orm(post)

        # Пост не горячий - имитируем нагрузку
        await asyncio.sleep(2)
        return PostRead.from_orm(post)

    async def list_user_posts(
        self,
        user_id: int,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> Sequence[PostRead]:
        posts = await self.repo.list_user_posts(user_id=user_id, limit=limit, offset=offset)
        result: list[PostRead] = []
        for post in posts:
            if await self._is_hot(post.created_at):
                # для горячих можно читать из Redis (если там есть) или класть туда
                cache_key = _post_cache_key(post.id)
                cached = await self.redis.hgetall(cache_key)
                if cached:
                    result.append(await self._deserialize_post(cached))
                else:
                    serialized = await self._serialize_post(post)
                    await self.redis.hset(cache_key, mapping=serialized)
                    await self.redis.expire(cache_key, HOT_PERIOD_MINUTES * 60)
                    result.append(PostRead.from_orm(post))
            else:
                # для старых — читаем из БД и разово спим
                await asyncio.sleep(2)
                result.append(PostRead.from_orm(post))
        return result

    async def count_user_posts(self, user_id: int) -> int:
        return await self.repo.count_user_posts(user_id=user_id)

