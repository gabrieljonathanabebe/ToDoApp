# tests/repositories/test_todo_repository.py

from sqlalchemy.orm import Session

from tests.db_seed import DbSeed
from mytodo.infra.db.models import ToDoModel, UserModel
from mytodo.infra.repositories import ToDoRepository


def test_create_todo_stores_todo(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    repo = ToDoRepository(db)
    overview = repo.create_todo(
        user_id=user.id,
        title="New To-Do",
    )
    saved_todo = db.get(ToDoModel, overview.id)
    assert saved_todo is not None
    assert saved_todo.user_id == user.id
    assert saved_todo.title == "New To-Do"
    assert saved_todo.position == 1
    assert saved_todo.created_at is not None
    assert saved_todo.updated_at == saved_todo.created_at
    assert overview.id == saved_todo.id


def test_delete_todo_removes_todo(
    db: Session,
    seed: DbSeed,
) -> None:
    todo = seed.todo()
    repo = ToDoRepository(db)
    deleted = repo.delete_todo(
        user_id=todo.user_id,
        todo_id=todo.id,
    )
    assert deleted is True
    assert db.get(ToDoModel, todo.id) is None


def test_get_todo_detail_returns_tasks(
    db: Session,
    seed: DbSeed,
) -> None:
    todo = seed.todo()
    seed.task(todo)
    seed.task(todo)
    repo = ToDoRepository(db)
    detail = repo.get_todo_detail(
        user_id=todo.user_id,
        todo_id=todo.id,
    )
    assert detail is not None
    assert len(detail.tasks) == 2
