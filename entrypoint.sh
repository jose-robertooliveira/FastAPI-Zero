#!/bin/sh

#run migrations
poetry run alembic upgrade head

#run application
poetry run uvicorn --host 0.0.0.0 --port 8000 fast_demo.app:app

#"poetry", "run", "uvicorn", "fast_demo.app:app", "--host", "0.0.0.0"
