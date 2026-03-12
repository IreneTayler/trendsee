from fastapi import APIRouter, Depends, HTTPException, status

from ..dependencies import get_user_service
from ..schemas import UserCreate, UserRead, UserUpdate, Token
from ..services.users import UserService


router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=Token, status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    user, token = await service.create_user(data)
    return Token(access_token=token)


@router.get("/{user_id}/token", response_model=Token)
async def get_token_for_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    token = await service.get_user_token(user_id)
    return Token(access_token=token)


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    user = await service.update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    await service.delete_user(user_id)

