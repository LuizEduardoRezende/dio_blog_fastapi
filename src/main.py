from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.controllers import post, auth
from src.database import database, engine, metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
app.include_router(auth.router)
