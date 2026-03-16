from datetime import datetime, timezone
from typing import Sequence

from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Post


class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_post(self, user_id: int, title: str, text: str) -> Post:
        post = Post(user_id=user_id, title=title, text=text)
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)
        return post

    async def get_post(self, post_id: int) -> Post | None:
        result = await self.session.execute(select(Post).where(Post.id == post_id))
        return result.scalar_one_or_none()

    async def update_post(
        self,
        post_id: int,
        *,
        title: str | None = None,
        text: str | None = None,
    ) -> Post | None:
        values: dict = {"updated_at": datetime.now(timezone.utc)}
        if title is not None:
            values["title"] = title
        if text is not None:
            values["text"] = text

        await self.session.execute(update(Post).where(Post.id == post_id).values(**values))
        await self.session.commit()
        return await self.get_post(post_id)

    async def delete_post(self, post_id: int) -> None:
        await self.session.execute(delete(Post).where(Post.id == post_id))
        await self.session.commit()

    async def list_user_posts(
        self,
        user_id: int,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> Sequence[Post]:
        stmt = (
            select(Post)
            .where(Post.user_id == user_id)
            .order_by(Post.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def count_user_posts(self, user_id: int) -> int:
        stmt = select(func.count()).select_from(Post).where(Post.user_id == user_id)
        result = await self.session.execute(stmt)
        return int(result.scalar_one())

