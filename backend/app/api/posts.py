from fastapi import APIRouter, Depends, HTTPException, Query, status

from ..dependencies import get_current_user, get_post_service
from ..models import User
from ..schemas import PostCreate, PostRead, PostUpdate
from ..services.posts import PostService


router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(
    data: PostCreate,
    current_user: User = Depends(get_current_user),
    service: PostService = Depends(get_post_service),
):
    return await service.create_post(current_user.id, data)


@router.patch("/{post_id}", response_model=PostRead)
async def update_post(
    post_id: int,
    data: PostUpdate,
    current_user: User = Depends(get_current_user),
    service: PostService = Depends(get_post_service),
):
    post = await service.get_post(post_id)
    if not post or post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    updated = await service.update_post(post_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return updated


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    current_user: User = Depends(get_current_user),
    service: PostService = Depends(get_post_service),
):
    post = await service.get_post(post_id)
    if not post or post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    await service.delete_post(post_id)


@router.get("/user/{user_id}", response_model=list[PostRead])
async def list_user_posts(
    user_id: int,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    service: PostService = Depends(get_post_service),
):
    return await service.list_user_posts(user_id=user_id, limit=limit, offset=offset)


@router.get("/{post_id}", response_model=PostRead)
async def get_post(
    post_id: int,
    service: PostService = Depends(get_post_service),
):
    post = await service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

