#!/usr/bin/env bash
set -e

# Tentar remover tabela alembic_version usando psql
echo "DROP TABLE IF EXISTS alembic_version CASCADE;" | psql $DATABASE_URL || true

# Aplicar migrações do zero
alembic upgrade head
uvicorn src.main:app --host 0.0.0.0 --port $PORT