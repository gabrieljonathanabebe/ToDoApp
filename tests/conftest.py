# tests/conftest.py

from collections.abc import Generator, Callable
from datetime import datetime, date, timezone
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from tests.db_seed import DbSeed
import tests.factories as factories
from mytodo.domain import Status
from mytodo.infra.db.base import Base
from mytodo.infra.db.models import UserModel, ToDoModel, TaskModel
import mytodo.infra.db.models
from mytodo.infra.repositories import TaskRepository


@pytest.fixture
def db() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


@pytest.fixture
def seed(db: Session) -> DbSeed:
    return DbSeed(db)


@pytest.fixture
def user_model(db: Session) -> UserModel:
    user = factories.make_user_model()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def todo_model(db: Session, user_model: UserModel) -> ToDoModel:
    old_time = datetime(2026, 1, 1, tzinfo=timezone.utc)
    todo = factories.make_todo_model(
        user_id=user_model.id,
        created_at=old_time,
        updated_at=old_time,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@pytest.fixture
def create_task(
    db: Session,
    todo_model: ToDoModel,
) -> Callable[..., TaskModel]:
    def _create_task(
        todo_id: str | None = None,
        position: int = 1,
        description: str = "Test task",
        priority: int = 1,
        status: Status = Status.open,
        due: date | None = None,
        notes: str | None = None,
    ) -> TaskModel:
        task = factories.make_task_model(
            todo_id=todo_id or todo_model.id,
            position=position,
            description=description,
            priority=priority,
            status=status,
            due=due,
            notes=notes,
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    return _create_task


@pytest.fixture
def task_model(
    create_task: Callable[..., TaskModel],
) -> Callable[..., TaskModel]:
    return create_task
