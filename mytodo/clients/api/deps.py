# mytodo/clients/api/deps.py

from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from mytodo.infra.db.session import SessionLocal
from mytodo.clients.api import http_results
from mytodo.core.results import Code, Result
from mytodo.core.services import UserService, ToDoService, TaskService
from mytodo.core.messages import ToDoMessage
from mytodo.domain import User
from mytodo.infra.repositories import UserRepository, ToDoRepository, TaskRepository


def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_service(
    db: Session = Depends(get_db_session),
) -> UserService:
    return UserService(user_repo=UserRepository(db))


def get_current_user(
    username: str,
    db: Session = Depends(get_db_session),
) -> User:
    repo = UserRepository(db)
    user = repo.get_by_username(username)
    if user is None:
        result = Result(Code.NOT_FOUND, ToDoMessage.user_not_found(username))
        http_results.raise_http_error(result)
    return user


def get_todo_service(db: Session = Depends(get_db_session)) -> ToDoService:
    return ToDoService(todo_repo=ToDoRepository(db))


def get_task_service(db: Session = Depends(get_db_session)) -> TaskService:
    return TaskService(
        task_repo=TaskRepository(db),
        todo_repo=ToDoRepository(db),
    )
