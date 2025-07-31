#!/usr/bin/env bash
set -e

# Limpar histórico de migrações e recriar do zero
alembic stamp base
alembic upgrade head
uvicorn src.main:app --host 0.0.0.0 --port $PORT