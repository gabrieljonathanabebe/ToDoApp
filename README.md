# MyToDo

MyToDo is a full-stack task management application built as a personal software engineering project.
It combines a FastAPI backend with a React frontend and focuses on clean architecture, practical usability, and iterative product development.

## Features

- User login and registration
- To-Do list overview
- Task creation, editing, sorting, and deletion
- List and grid views for task details
- Dashboard with key productivity metrics
- Session and navigation persistence
- PostgreSQL-backed persistence
- Docker-based local runtime
- Alembic database migrations

## Tech Stack

- **Backend:** FastAPI, Pydantic, SQLAlchemy
- **Frontend:** React, Vite
- **Database:** PostgreSQL
- **Migrations:** Alembic
- **Tooling:** pytest, pre-commit, black, Docker Compose

## Project Structure

```bash
mytodo/
  clients/
    api/        # FastAPI routes, schemas, dependencies
    web/        # React/Vite frontend
  core/         # services, application results, errors, messages
  domain/       # Pydantic domain models and computes domain properties
  infra/
    adapters/   # mapping between ORM/domain/API response models
    db/         # SQLAlchemy base, session and ORM models
    repositories/
migrations/     # Alembic migration environment and versions
docs/
tests/
```

- **domain** contains the core business models and computed properties
- **core** contains service-layer use cases, result types, errors and messages
- **infra** contains database models, repositories and adapters
- **clients/api** exposes the FastAPI HTTP API
- **clients/web** contains the react frontend
- **migrations** contains Alembic migration setup and schema versions

## Getting started

### 1. Create and active a virtual environment

```bash
/opt/homebrew/bin/python3.13 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements-dev.txt
```

### 3. Start PostgreSQL with Docker Compose
```bash
docker compose up -d db
```
For local development outside Docker, `.env` should point to the exposed local database port, for example:
```env
DATABASE_URL=postgresql+psycopg://mytodo:mytodo@localhost:5433/mytodo
FRONTEND_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

### 4. Run database migrations
```bash
alembic upgrade head
```

### 5. Start the backend locally

```bash
python -m uvicorn mytodo.clients.api.app:app --reload
```

### 6. Start the frontend locally

```bash
cd mytodo/clients/web
npm install
npm run dev
```

## Docker Runtime

The project includes a Docker Compose setup for local integration testing with:
- PostgreSQL
- FastAPI backend
- Vite frontend

Start the full stack with:

```bash
docker compose up --build
```
Run migration inside the backend container with:
```bash
docker compose exec backend alembic upgrade head
```

The local frontend is available at:
```txt
http://localhost:5173
```

The backend API docs are available at:
```txt
http://localhost:8000/docs
```

## Testing and Checks

Run backend tests with:

```bash
pytest -v
```

Run frontend linting and production build checks with:
```bash
npm --prefix mytodo/clients/web run lint
npm --prefix mytodo/clients/web run build
```

Run pre-commit checks with:

```bash
pre-commit run --all-files
```

## Current Deployment

MyToDo v0.2.0 is currently deployed as a test release at:

- Frontend: https://mytodo.jonathanabebe.dev
- API docs: https://api.mytodo.jonathanabebe.dev/docs

The deployment runs on AWS EC2 with Docker Compose, PostgresQL, Alembic migrations and Caddy for HTTPS/reverse proxy.


## Roadmap

Planned next steps include:

- Replace prototype authentication with a safer user management flow
- Improve responsive layout for mobile and tablet
- Add CD automation
- Add backups or managed database option


## Screenshots

The screenshots below were captured for `v0.1.0`. They remain visually representative for `v0.2.0`, which primarily changes persistence, backend architecture, and frontend data flow rather than the UI design.


### To-Do-Detail List View

<img src="docs/images/screenshots/todo-detail-list-view-v0.1.0.png" alt="To-Do detail list view" width="900" />

### Dashboard

<img src="docs/images/screenshots/dashboard-v0.1.0.png" alt="Dashboard view" width="900" />
