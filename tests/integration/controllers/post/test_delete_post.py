import pytest_asyncio
from fastapi import status
from httpx import AsyncClient


@pytest_asyncio.fixture(autouse=True)
async def populate_posts(db):
    from src.schemas.post import PostIn
    from src.services.post import PostService

    service = PostService()
    await service.create(PostIn(title="Post 1", content="Content 1", published=True))
    await service.create(PostIn(title="Post 2", content="Content 2", published=True))
    await service.create(PostIn(title="Post 3", content="Content 3", published=False))


async def test_delete_post_success(client: AsyncClient, access_token: str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1  # Assuming this post exists from the fixture

    # When
    response = await client.delete(f"/posts/{post_id}", headers=headers)

    # Then
    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_delete_post_not_authenticated_fail(client: AsyncClient):
    # Given
    post_id = 1  # Assuming this post exists from the fixture

    # When
    response = await client.delete(f"/posts/{post_id}")

    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_delete_post_not_found_fail(client: AsyncClient, access_token: str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 999  # Assuming this post does not exist

    # When
    response = await client.delete(f"/posts/{post_id}", headers=headers)

    # Then
    assert response.status_code == status.HTTP_404_NOT_FOUND
