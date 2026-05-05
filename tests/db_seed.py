# tests/db_seed.py

from datetime import date, datetime, timezone
from uuid import uuid4

from sqlalchemy.orm import Session

from mytodo.infra.db.models import UserModel, ToDoModel, TaskModel
from mytodo.domain import Status


class DbSeed:
    def __init__(self, db: Session):
        self.db = db

    def _save(self, model):
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model

    def user(
        self,
        username: str = "test-user",
        password: str = "hashed-password",
    ) -> UserModel:
        user = UserModel(
            id=str(uuid4()),
            username=username,
            password=password,
            created_at=datetime.now(timezone.utc),
        )
        return self._save(user)

    def todo(
        self,
        user: UserModel | None = None,
        title: str = "Test To-Do",
        position: int = 1,
    ) -> ToDoModel:
        user = user or self.user()
        now = datetime.now(timezone.utc)
        todo = ToDoModel(
            id=str(uuid4()),
            user_id=user.id,
            position=position,
            title=title,
            created_at=now,
            updated_at=now,
        )
        return self._save(todo)

    def task(
        self,
        todo: ToDoModel,
        description: str = "Test task",
        position: int = 1,
        priority: int = 1,
        status: Status = Status.open,
        due: date | None = None,
        notes: str | None = None,
    ) -> TaskModel:
        now = datetime.now(timezone.utc)
        task = TaskModel(
            id=str(uuid4()),
            todo_id=todo.id,
            position=position,
            description=description,
            priority=priority,
            status=status.value,
            due=due,
            created_at=now,
            updated_at=now,
            completed_at=None,
            notes=notes,
        )
        return self._save(task)
