from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from src.controllers import post, auth
from src.database import database, engine, metadata
from src.exceptions import NotFoundPostError


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Operações para autenticação.",
    },
    {
        "name": "posts",
        "description": "Operações para manter posts",
        "externalDocs": {
            "description": "Documentação externa para Posts.api",
            "url": "https://post-api.com/",
        },
    },
]

servers = [
    {"url": "http://localhost:8000", "description": "Ambiente de desenvolvimento"},
    {"url": "https://api.example.com", "description": "Ambiente de produção"},
]

app = FastAPI(
    lifespan=lifespan,
    title="DIO Blog API",
    description="""
DIO blog API ajuda a você criar o seu blog pessoal.

## Posts

Você será capaz de fazer:
* **Criar posts**.
* **Recuperar posts**.
* **Recuperar posts por ID**.
* **Atualizar posts**.
* **Deletar posts**.


Você pode autenticar usuários para acessar as operações de posts.
    """,
    version="1.0.2",
    openapi_tags=tags_metadata,
    servers=servers,
    # redoc_url=None, # disable ReDoc documentation
    # docs_url=None,  # disable Swagger UI documentation
    # openapi_url = None # disable OpenAPI documentation
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

app.include_router(post.router, tags=["posts"])
app.include_router(auth.router, tags=["auth"])


@app.exception_handler(NotFoundPostError)
async def bot_found_post_exception_handler(request: Request, exc: NotFoundPostError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": exc.message}
    )
