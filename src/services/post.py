from databases.interfaces import Record

from src.schemas.post import PostIn
from src.schemas.post import PostUpdateIn
from src.models.post import posts
from src.database import database
from src.exceptions import NotFoundPostError


class PostService:
    async def read_all(
        self, published: bool | None = None, limit: int = 10, skip: int = 0
    ) -> list[Record]:
        query = posts.select().limit(limit).offset(skip)
        if published is not None:
            query = query.where(posts.c.published == published)
        return await database.fetch_all(query)

    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def create(self, post: PostIn) -> Record:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )
        post_id = await database.execute(command)
        return await self.__get_by_id(post_id)

    async def update(self, id: int, post: PostUpdateIn) -> Record:
        total = await self.count(id)
        if not total:
            raise NotFoundPostError
        data = post.model_dump(exclude_unset=True)
        command = posts.update().where(posts.c.id == id).values(**data)
        await database.execute(command)

        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:
        # Verificar se o post existe antes de deletar
        total = await self.count(id)
        if not total:
            raise NotFoundPostError

        command = posts.delete().where(posts.c.id == id)
        await database.execute(command)

    async def count(self, id: int) -> int:
        query = "select count(id) as total from posts where id = :id"
        result = await database.fetch_one(query, values={"id": id})
        return result["total"]

    async def __get_by_id(self, id: int) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise NotFoundPostError
        return post
