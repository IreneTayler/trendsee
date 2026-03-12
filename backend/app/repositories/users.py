from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, name: str) -> User:
        user = User(name=name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user(self, user_id: int) -> User | None:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def update_user_name(self, user_id: int, name: str) -> User | None:
        await self.session.execute(
            update(User).where(User.id == user_id).values(name=name),
        )
        await self.session.commit()
        return await self.get_user(user_id)

    async def delete_user(self, user_id: int) -> None:
        await self.session.execute(delete(User).where(User.id == user_id))
        await self.session.commit()

