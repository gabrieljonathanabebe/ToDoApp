# mytodo/infra/repositories/task_repository.py

from collections.abc import Callable
from datetime import date, datetime
from uuid import uuid4

from sqlalchemy import select

from mytodo.domain import Status, Task
from mytodo.infra.adapters import TaskAdapter
from mytodo.infra.db.models import TaskModel
from mytodo.infra.repositories import BaseRepository


class TaskRepository(BaseRepository):
    def _shift_task_positions_down(self, todo_id: str) -> None:
        stmt = select(TaskModel).where(TaskModel.todo_id == todo_id)
        task_models = list(self.db.execute(stmt).scalars().all())
        for task_model in task_models:
            task_model.position += 1

    def _update_task(
        self,
        todo_id: str,
        task_id: str,
        apply_update: Callable[[TaskModel, datetime], None],
    ) -> Task | None:
        task_model = self._get_task_model_for_todo(todo_id, task_id)
        if task_model is None:
            return None
        now = self._now()
        apply_update(task_model, now)
        task_model.updated_at = now
        self._touch_todo_updated_at(todo_id, now)
        self._commit_update(task_model)
        return TaskAdapter.model_to_domain(task_model)

    def create_task(
        self,
        todo_id: str,
        description: str,
        priority: int,
        due: date | None,
        notes: str | None,
    ) -> Task:
        now = self._now()
        self._shift_task_positions_down(todo_id)
        task_model = TaskModel(
            id=str(uuid4()),
            todo_id=todo_id,
            position=1,
            description=description,
            priority=priority,
            status=Status.open.value,
            due=due,
            created_at=now,
            updated_at=now,
            completed_at=None,
            notes=notes,
        )
        self._touch_todo_updated_at(todo_id, now)
        self._commit_create(task_model)
        return TaskAdapter.model_to_domain(task_model)

    def delete_task(self, todo_id: str, task_id: str) -> bool:
        task_model = self._get_task_model_for_todo(todo_id, task_id)
        if task_model is None:
            return False
        self._touch_todo_updated_at(todo_id)
        self._commit_delete(task_model)
        return True

    def update_task_status(
        self,
        todo_id: str,
        task_id: str,
        status: Status,
    ) -> Task | None:
        def apply_status(task_model: TaskModel, now: datetime) -> None:
            task_model.status = status.value
            task_model.completed_at = now if status == Status.done else None

        return self._update_task(todo_id, task_id, apply_status)

    def update_task_description(
        self,
        todo_id: str,
        task_id: str,
        description: str,
    ) -> Task | None:
        def apply_description(task_model: TaskModel, now: datetime) -> None:
            task_model.description = description

        return self._update_task(todo_id, task_id, apply_description)

    def update_task_priority(
        self,
        todo_id: str,
        task_id: str,
        priority: int,
    ) -> Task | None:
        def apply_priority(task_model: TaskModel, now: datetime) -> None:
            task_model.priority = priority

        return self._update_task(todo_id, task_id, apply_priority)

    def update_task_due(
        self,
        todo_id: str,
        task_id: str,
        due: date | None,
    ) -> Task | None:
        def apply_due(task_model: TaskModel, now: datetime) -> None:
            task_model.due = due

        return self._update_task(todo_id, task_id, apply_due)

    def update_task_order(
        self,
        todo_id: str,
        positions_by_task_id: dict[str, int],
    ) -> list[Task] | None:
        stmt = select(TaskModel).where(
            TaskModel.todo_id == todo_id, TaskModel.id.in_(positions_by_task_id.keys())
        )
        task_models = list(self.db.execute(stmt).scalars().all())
        if len(task_models) != len(positions_by_task_id):
            return None
        now = self._now()
        for task_model in task_models:
            task_model.position = positions_by_task_id[task_model.id]
            task_model.updated_at = now
        self._touch_todo_updated_at(todo_id, now)
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        ordered_stmt = (
            select(TaskModel)
            .where(TaskModel.todo_id == todo_id)
            .order_by(TaskModel.position.asc(), TaskModel.created_at.desc())
        )
        ordered_models = list(self.db.execute(ordered_stmt).scalars().all())
        return TaskAdapter.models_to_domain(ordered_models)
