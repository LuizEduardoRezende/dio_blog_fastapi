# DIO Blog API

Uma API REST completa para gerenciamento de blog pessoal desenvolvida com FastAPI, criada como parte da formação Python Backend da Digital Innovation One.

## 🚀 Sobre o Projeto

A DIO Blog API é uma aplicação assíncrona que permite criar, gerenciar e publicar posts de blog. Com autenticação JWT e operações CRUD completas, esta API fornece uma base sólida para desenvolvimento de blogs pessoais ou corporativos.

### ✨ Funcionalidades

- 📝 **CRUD de Posts**: Criação, leitura, atualização e exclusão de posts
- 🔐 **Autenticação JWT**: Sistema seguro de autenticação
- 📊 **Banco de Dados Assíncrono**: Suporte a SQLite e PostgreSQL
- 🔄 **Migrações**: Gerenciamento de esquema com Alembic
- 📖 **Documentação Automática**: Swagger UI e ReDoc
- 🌐 **CORS**: Configuração para desenvolvimento frontend
- ☁️ **Deploy Ready**: Configurado para deploy no Render

## 🛠️ Tecnologias Utilizadas

- **FastAPI** - Framework web moderno para APIs
- **SQLAlchemy** - ORM para manipulação do banco de dados
- **Alembic** - Ferramenta para migrações de banco
- **Databases** - Suporte assíncrono para bancos de dados
- **PyJWT** - Implementação de JSON Web Tokens
- **Uvicorn** - Servidor ASGI para aplicações assíncronas
- **Pydantic** - Validação de dados e configurações
- **Pytest** - Framework de testes

## 📋 Pré-requisitos

- Python 3.13+
- Poetry (gerenciador de dependências)

## ⚙️ Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd dio-blog
```

2. **Instale as dependências**
```bash
poetry install
```

3. **Configure o ambiente virtual**
```bash
poetry shell
```

4. **Execute as migrações**
```bash
alembic upgrade head
```

## 🚀 Executando a Aplicação

### Desenvolvimento
```bash
uvicorn src.main:app --reload
```

### Produção
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints Principais

#### Autenticação
- `POST /auth/login` - Realiza login e retorna token JWT

#### Posts
- `GET /posts` - Lista todos os posts
- `POST /posts` - Cria um novo post
- `GET /posts/{id}` - Busca post por ID
- `PUT /posts/{id}` - Atualiza um post
- `DELETE /posts/{id}` - Remove um post

## 🗄️ Estrutura do Banco

## 🧪 Executando Testes

```bash
pytest
```

## 📁 Estrutura do Projeto

```
dio-blog/
├── src/
│   ├── controllers/     # Controladores/Rotas
│   ├── models/         # Modelos do banco de dados
│   ├── schemas/        # Schemas Pydantic
│   ├── services/       # Lógica de negócio
│   ├── views/          # Modelos de resposta
│   ├── config.py       # Configurações
│   ├── database.py     # Configuração do banco
│   ├── exceptions.py   # Exceções customizadas
│   ├── main.py         # Aplicação principal
│   └── security.py     # Autenticação e segurança
├── migrations/         # Migrações Alembic
├── tests/             # Testes automatizados
├── alembic.ini        # Configuração Alembic
├── pyproject.toml     # Dependências e configurações
└── render-deploy.sh   # Script de deploy
```

## 🔐 Autenticação

A API utiliza JWT (JSON Web Tokens) para autenticação. Para acessar endpoints protegidos:

1. Faça login no endpoint `/auth/login`
2. Use o token retornado no header `Authorization: Bearer <token>`

## 🌐 Deploy

### Render
O projeto está configurado para deploy automático no Render:

1. Conecte seu repositório ao Render
2. Configure as variáveis de ambiente necessárias
3. O script `render-deploy.sh` será executado automaticamente

## 🔧 Configuração

Configure as seguintes variáveis de ambiente:

```env
DATABASE_URL=sqlite:///./blog.db
SECRET_KEY=sua-chave-secreta-jwt
ALGORITHM=HS256
```

