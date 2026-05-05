# mytodo/infra/repositories/base.py

from datetime import datetime, timezone
from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from mytodo.infra.db.models import TaskModel, ToDoModel, UserModel


ModelT = TypeVar("ModelT")


class BaseRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    @staticmethod
    def _now() -> datetime:
        return datetime.now(timezone.utc)

    def _commit_create(self, model: ModelT) -> None:
        try:
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
        except Exception:
            self.db.rollback()
            raise

    def _commit_update(self, model: ModelT) -> None:
        try:
            self.db.commit()
            self.db.refresh(model)
        except Exception:
            self.db.rollback()
            raise

    def _commit_delete(self, model: object) -> None:
        try:
            self.db.delete(model)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def _get_user_model_by_username(self, username: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.username == username)
        return self.db.execute(stmt).scalar_one_or_none()

    def _get_todo_model_for_user(self, user_id: str, todo_id: str) -> ToDoModel | None:
        stmt = select(ToDoModel).where(
            ToDoModel.user_id == user_id, ToDoModel.id == todo_id
        )
        return self.db.execute(stmt).scalar_one_or_none()

    def _get_todo_id_for_user(
        self,
        user_id: str,
        todo_id: str,
    ) -> str | None:
        stmt = select(ToDoModel.id).where(
            ToDoModel.user_id == user_id,
            ToDoModel.id == todo_id,
        )
        return self.db.execute(stmt).scalar_one_or_none()

    def _get_task_model_for_todo(
        self,
        todo_id: str,
        task_id: str,
    ) -> TaskModel | None:
        stmt = select(TaskModel).where(
            TaskModel.todo_id == todo_id,
            TaskModel.id == task_id,
        )
        return self.db.execute(stmt).scalar_one_or_none()

    def _touch_todo_updated_at(self, todo_id: str, now: datetime | None = None) -> None:
        todo_model = self.db.get(ToDoModel, todo_id)
        if todo_model is not None:
            todo_model.updated_at = now or self._now()
