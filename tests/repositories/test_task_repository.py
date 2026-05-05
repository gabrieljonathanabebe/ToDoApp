# tests/repositories/test_task_repository.py

from datetime import date

from sqlalchemy.orm import Session
import pytest

from mytodo.domain import Status
from mytodo.infra.db.models import ToDoModel, TaskModel
from mytodo.infra.repositories import TaskRepository


def test_create_task_stores_task_and_touches_todo(
    db: Session, todo_model: ToDoModel
) -> None:
    old_todo_updated_at = todo_model.updated_at
    repo = TaskRepository(db)
    task = repo.create_task(
        todo_id=todo_model.id,
        description="Test task",
        priority=2,
        due=date(2026, 7, 1),
        notes="Important",
    )
    saved_task = db.get(TaskModel, task.id)
    db.refresh(todo_model)
    assert saved_task is not None
    assert saved_task.todo_id == todo_model.id
    assert saved_task.position == 1
    assert saved_task.description == "Test task"
    assert saved_task.priority == 2
    assert saved_task.status == Status.open.value
    assert saved_task.due == date(2026, 7, 1)
    assert saved_task.notes == "Important"
    assert todo_model.updated_at > old_todo_updated_at


def test_delete_task_removes_task(
    db: Session,
    todo_model: ToDoModel,
    create_task,
) -> None:
    task = create_task()
    repo = TaskRepository(db)
    deleted_task = repo.delete_task(todo_model.id, task.id)
    assert deleted_task is True
    assert db.get(TaskModel, task.id) is None


def test_update_task_description_updates_task(
    db: Session,
    todo_model: ToDoModel,
    create_task,
) -> None:
    task = create_task(description="Old description")
    old_task_updated_at = task.updated_at
    repo = TaskRepository(db)
    updated_task = repo.update_task_description(
        todo_id=todo_model.id, task_id=task.id, description="New description"
    )
    saved_task = db.get(TaskModel, task.id)
    assert updated_task is not None
    assert saved_task is not None
    assert updated_task.description == "New description"
    assert saved_task.description == "New description"
    assert saved_task.updated_at > old_task_updated_at


def test_update_task_returns_none_when_task_is_missing(
    db: Session,
    todo_model: ToDoModel,
) -> None:
    repo = TaskRepository(db)
    missing_task = repo.update_task_description(
        todo_id=todo_model.id,
        task_id="missing-id",
        description="New description",
    )
    assert missing_task is None


@pytest.mark.parametrize(
    "status, expected_completed",
    [
        (Status.done, True),
        (Status.open, False),
        (Status.cancelled, False),
    ],
)
def test_update_task_status_updates_completed_at(
    db: Session,
    todo_model: ToDoModel,
    create_task,
    status: Status,
    expected_completed: bool,
) -> None:
    task = create_task()
    repo = TaskRepository(db)
    updated_task = repo.update_task_status(
        todo_id=todo_model.id,
        task_id=task.id,
        status=status,
    )
    saved_task = db.get(TaskModel, task.id)
    assert updated_task is not None
    assert saved_task is not None
    assert saved_task.status == status.value
    assert (saved_task.completed_at is not None) is expected_completed


def test_update_task_order_updates_position_and_returns_ordered_tasks(
    db: Session,
    todo_model: ToDoModel,
    create_task,
) -> None:
    first_task = create_task(description="First")
    second_task = create_task(description="Second")
    repo = TaskRepository(db)
    tasks = repo.update_task_order(
        todo_id=todo_model.id,
        positions_by_task_id={
            first_task.id: 2,
            second_task.id: 1,
        },
    )
    assert tasks is not None
    assert [task.id for task in tasks] == [second_task.id, first_task.id]
