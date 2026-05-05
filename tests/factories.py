# tests/factories.py

from uuid import uuid4
from datetime import datetime, date, timezone

from mytodo.infra.db.models import UserModel, ToDoModel, TaskModel
from mytodo.domain import Priority, Status, Task


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def make_task(
    id: str | None = None,
    position: int = 1,
    description: str = "Test task",
    priority: Priority = Priority.low,
    status: Status = Status.open,
    due: date | None = None,
    created_at: datetime | None = None,
    updated_at: datetime | None = None,
    completed_at: datetime | None = None,
    notes: str | None = None,
) -> Task:
    created_at = created_at or utc_now()
    updated_at = updated_at or created_at
    return Task(
        id=id or str(uuid4()),
        position=position,
        description=description,
        priority=priority,
        status=status,
        due=due,
        created_at=created_at,
        updated_at=updated_at,
        completed_at=completed_at,
        notes=notes,
    )


def make_user_model(
    id: str | None = None,
    username: str = "test-user",
    password: str = "hashed-password",
    created_at: datetime | None = None,
) -> UserModel:
    now = created_at or utc_now()
    return UserModel(
        id=id or str(uuid4()), username=username, password=password, created_at=now
    )


def make_todo_model(
    id: str | None = None,
    user_id: str = "test-user-id",
    position: int = 1,
    title: str = "Test To-Do",
    created_at: datetime | None = None,
    updated_at: datetime | None = None,
) -> ToDoModel:
    created_at = created_at or utc_now()
    updated_at = updated_at or created_at
    return ToDoModel(
        id=id or str(uuid4()),
        user_id=user_id,
        position=position,
        title=title,
        created_at=created_at,
        updated_at=updated_at,
    )


def make_task_model(
    id: str | None = None,
    todo_id: str = "test-todo-id",
    position: int = 1,
    description: str = "Test task",
    priority: int = 1,
    status: Status = Status.open,
    due: date | None = None,
    created_at: datetime | None = None,
    updated_at: datetime | None = None,
    completed_at: datetime | None = None,
    notes: str | None = None,
) -> TaskModel:
    created_at = created_at or utc_now()
    updated_at = updated_at or created_at
    return TaskModel(
        id=id or str(uuid4()),
        todo_id=todo_id,
        position=position,
        description=description,
        priority=priority,
        status=status.value,
        due=due,
        created_at=created_at,
        updated_at=updated_at,
        completed_at=completed_at,
        notes=notes,
    )
