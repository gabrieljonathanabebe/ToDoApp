from datetime import date

from sqlalchemy.orm import Session

from mytodo.core.results import Code
from mytodo.core.services import TaskService, ToDoService
from mytodo.domain import Status
from mytodo.infra.repositories import TaskRepository, ToDoRepository
from tests.db_seed import DbSeed


def make_todo_service(db: Session) -> ToDoService:
    return ToDoService(todo_repo=ToDoRepository(db))


def make_task_service(db: Session) -> TaskService:
    return TaskService(
        task_repo=TaskRepository(db),
        todo_repo=ToDoRepository(db),
    )


def test_get_todo_summaries_returns_ok_and_data(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    todo = seed.todo(user=user)
    seed.task(todo)

    res = make_todo_service(db).get_todo_summaries(user.id)

    assert res.code == Code.OK
    assert res.data is not None
    assert len(res.data) == 1
    assert res.data[0].task_count == 1


def test_create_todo_success_returns_workspace(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()

    res = make_todo_service(db).create_todo(user.id, "New To-Do")

    assert res.code == Code.CREATED
    assert res.data is not None
    assert [todo.title for todo in res.data.todos] == ["New To-Do"]


def test_create_todo_duplicate_returns_already_exists(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    seed.todo(user=user, title="New To-Do")

    res = make_todo_service(db).create_todo(user.id, "New To-Do")

    assert res.code == Code.ALREADY_EXISTS
    assert res.data is None


def test_delete_todo_success_returns_workspace(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    todo = seed.todo(user=user)

    res = make_todo_service(db).delete_todo(user.id, todo.id)

    assert res.code == Code.OK
    assert res.data is not None
    assert res.data.todos == []


def test_delete_todo_missing_returns_not_found(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()

    res = make_todo_service(db).delete_todo(user.id, "missing-id")

    assert res.code == Code.NOT_FOUND
    assert res.data is None


def test_create_task_success_returns_workspace(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    todo = seed.todo(user=user)

    res = make_task_service(db).create_task(
        user_id=user.id,
        todo_id=todo.id,
        description="Test Desc",
        priority=2,
        due=date(2026, 7, 1),
        notes="Important",
    )

    assert res.code == Code.CREATED
    assert res.data is not None
    assert res.data.todos[0].tasks[0].description == "Test Desc"
    assert res.data.todos[0].task_count == 1


def test_update_task_status_success_returns_workspace(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    todo = seed.todo(user=user)
    task = seed.task(todo)

    res = make_task_service(db).update_task_status(
        user_id=user.id,
        todo_id=todo.id,
        task_id=task.id,
        status=Status.done.value,
    )

    assert res.code == Code.OK
    assert res.data is not None
    assert res.data.todos[0].tasks[0].status == Status.done
    assert res.data.todos[0].done_task_count == 1


def test_delete_task_success_returns_workspace(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    todo = seed.todo(user=user)
    task = seed.task(todo)

    res = make_task_service(db).delete_task(user.id, todo.id, task.id)

    assert res.code == Code.OK
    assert res.data is not None
    assert res.data.todos[0].tasks == []


def test_update_task_missing_returns_not_found(
    db: Session,
    seed: DbSeed,
) -> None:
    user = seed.user()
    todo = seed.todo(user=user)

    res = make_task_service(db).update_task_description(
        user_id=user.id,
        todo_id=todo.id,
        task_id="missing-id",
        description="Updated",
    )

    assert res.code == Code.NOT_FOUND
    assert res.data is None
