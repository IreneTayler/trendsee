from fastapi import HTTPException, status

from ..repositories.users import UserRepository
from ..schemas import UserCreate, UserRead, UserUpdate
from ..core.security import create_access_token


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, data: UserCreate) -> tuple[UserRead, str]:
        user = await self.repo.create_user(name=data.name)
        token = create_access_token({"sub": str(user.id)})
        # Pydantic v1: use from_orm (enabled via from_attributes = True)
        return UserRead.from_orm(user), token

    async def get_user_token(self, user_id: int) -> str:
        # Генерируем JWT только если пользователь существует
        user = await self.repo.get_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return create_access_token({"sub": str(user.id)})

    async def update_user(self, user_id: int, data: UserUpdate) -> UserRead | None:
        user = await self.repo.update_user_name(user_id, data.name)
        if not user:
            return None
        return UserRead.from_orm(user)

    async def delete_user(self, user_id: int) -> None:
        await self.repo.delete_user(user_id)

