from fastapi import status, APIRouter, Depends, HTTPException
from src.schemas.post import PostIn, PostUpdateIn
from src.views.post import PostOut
from src.services.post import PostService
from src.security import login_required
from src.exceptions import NotFoundPostError


router = APIRouter(prefix="/posts", dependencies=[Depends(login_required)])

service = PostService()


@router.get("/{post_id}", response_model=PostOut)
async def read_post(post_id: int):
    return await service.read(post_id)


@router.get("/", response_model=list[PostOut])
async def read_all_posts(published: str, limit: int, skip: int = 0):
    # Converter string para boolean
    published_bool = (
        published.lower() == "on" if isinstance(published, str) else published
    )
    return await service.read_all(published_bool, limit, skip)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    return await service.create(post)


@router.patch("/{post_id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def update_post(post_id: int, post: PostUpdateIn):
    return await service.update(post_id, post)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    await service.delete(post_id)
