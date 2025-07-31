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


async def test_update_post_success(client: AsyncClient, access_token: str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 1
    data = {"title": "Updated Post"}

    # When
    response = await client.patch(f"/posts/{post_id}", headers=headers, json=data)

    # Then
    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert content["title"] == data["title"]


async def test_update_post_not_authenticated_fail(client: AsyncClient):
    # Given
    post_id = 1

    # When
    response = await client.patch(f"/posts/{post_id}")

    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_update_post_not_found_fail(client: AsyncClient, access_token: str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    post_id = 999  # Assuming this post does not exist
    data = {"title": "Updated Post 999"}

    # When
    response = await client.patch(f"/posts/{post_id}", headers=headers, json=data)

    # Then
    assert response.status_code == status.HTTP_404_NOT_FOUND
