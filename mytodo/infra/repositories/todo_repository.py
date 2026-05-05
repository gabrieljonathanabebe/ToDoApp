# mytodo/infra/repositories/todo_repository.py

from uuid import uuid4

from sqlalchemy import func, select

from mytodo.infra.repositories import BaseRepository
from mytodo.domain import ToDoDetail, ToDoWorkspace
from mytodo.infra.adapters import ToDoAdapter
from mytodo.infra.db.models import TaskModel, ToDoModel


class ToDoRepository(BaseRepository):
    def _shift_todo_positions_down(self, user_id: str) -> None:
        stmt = select(ToDoModel).where(ToDoModel.user_id == user_id)
        todo_models = list(self.db.execute(stmt).scalars().all())

        for todo_model in todo_models:
            todo_model.position += 1

    # ===== GETTERS ===========================================================
    def get_todo_id(self, user_id: str, todo_id: str) -> str | None:
        return self._get_todo_id_for_user(user_id, todo_id)

    def get_workspace(self, user_id: str) -> ToDoWorkspace:
        todo_stmt = (
            select(ToDoModel)
            .where(ToDoModel.user_id == user_id)
            .order_by(ToDoModel.position.asc(), ToDoModel.created_at.asc())
        )
        todo_orms = list(self.db.execute(todo_stmt).scalars().all())
        todo_ids = [todo.id for todo in todo_orms]
        if not todo_ids:
            return ToDoWorkspace(todos=[])
        task_stmt = (
            select(TaskModel)
            .where(TaskModel.todo_id.in_(todo_ids))
            .order_by(TaskModel.position.asc(), TaskModel.created_at.desc())
        )
        task_orms = list(self.db.execute(task_stmt).scalars().all())
        task_orms_by_todo_id: dict[str, list[TaskModel]] = {
            todo_id: [] for todo_id in todo_ids
        }
        for task_orm in task_orms:
            task_orms_by_todo_id[task_orm.todo_id].append(task_orm)
        return ToDoAdapter.orms_to_workspace_domain(
            todo_orms=todo_orms,
            task_orms_by_todo_id=task_orms_by_todo_id,
        )

    def get_todo_detail(
        self,
        user_id: str,
        todo_id: str,
    ) -> ToDoDetail | None:
        todo_model = self._get_todo_model_for_user(user_id, todo_id)
        if todo_model is None:
            return None
        stmt = (
            select(TaskModel)
            .where(TaskModel.todo_id == todo_model.id)
            .order_by(TaskModel.position.asc(), TaskModel.created_at.asc())
        )
        task_models = list(self.db.execute(stmt).scalars().all())
        return ToDoAdapter.orm_to_detail_domain(todo_model, task_models)

    # ===== SETTERS ===========================================================
    def create_todo(self, user_id: str, title: str) -> ToDoDetail:
        now = self._now()
        self._shift_todo_positions_down(user_id)
        todo_orm = ToDoModel(
            id=str(uuid4()),
            user_id=user_id,
            position=1,
            title=title,
            created_at=now,
            updated_at=now,
        )
        self._commit_create(todo_orm)
        return ToDoAdapter.orm_to_detail_domain(todo_orm=todo_orm, task_orms=[])

    def delete_todo(self, user_id: str, todo_id: str) -> bool:
        todo_model = self._get_todo_model_for_user(user_id, todo_id)
        if todo_model is None:
            return False
        self._commit_delete(todo_model)
        return True
