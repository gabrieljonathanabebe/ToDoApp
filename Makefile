.PHONY: test lint build check docker-up docker-down docker-logs migrate db-shell

test:
	python -m pytest

lint:
	npm --prefix mytodo/clients/web run lint

build:
	npm --prefix mytodo/clients/web run build

check: test lint build

docker-up:
	docker compose up --build

docker-up-detached:
	docker compose up -d --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f

migrate:
	docker compose exec backend alembic upgrade head

db-shell:
	docker compose exec db psql -U mytodo -d mytodo
