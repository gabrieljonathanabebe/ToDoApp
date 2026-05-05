# mytodo/core/services/task.py

from datetime import date

from mytodo.core.services.base import BaseService
from mytodo.core.errors import NotFoundError, InvalidInputError
from mytodo.core.messages import ToDoMessage
from mytodo.core.responses import Success, created, ok, resultify
from mytodo.domain import Status, Priority, ToDoWorkspace
from mytodo.infra.repositories import TaskRepository, ToDoRepository


class TaskService(BaseService):
    def __init__(
        self,
        task_repo: TaskRepository,
        todo_repo: ToDoRepository,
    ):
        super().__init__(todo_repo=todo_repo)
        self.task_repo = task_repo

    @resultify
    def create_task(
        self,
        user_id: str,
        todo_id: str,
        description: str,
        priority: int,
        due: date | None,
        notes: str | None,
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        task = self.task_repo.create_task(
            todo_id=valid_todo_id,
            description=description,
            priority=priority,
            due=due,
            notes=notes,
        )
        workspace = self.todo_repo.get_workspace(user_id)
        return created(ToDoMessage.task_created(task.id), data=workspace)

    @resultify
    def delete_task(
        self, user_id: str, todo_id: str, task_id: str
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        is_deleted = self.task_repo.delete_task(valid_todo_id, task_id)
        if not is_deleted:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(ToDoMessage.task_deleted(task_id), data=workspace)

    @resultify
    def update_task_status(
        self,
        user_id: str,
        todo_id: str,
        task_id: str,
        status: str,
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        try:
            target_status = Status(status)
        except ValueError:
            raise InvalidInputError(ToDoMessage.invalid_status(status))
        task = self.task_repo.update_task_status(
            todo_id=valid_todo_id,
            task_id=task_id,
            status=target_status,
        )
        if task is None:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(
            ToDoMessage.task_status_updated(task.id, task.status.value),
            data=workspace,
        )

    @resultify
    def update_task_description(
        self, user_id: str, todo_id: str, task_id: str, description: str
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        task = self.task_repo.update_task_description(
            todo_id=valid_todo_id,
            task_id=task_id,
            description=description,
        )
        if task is None:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(ToDoMessage.task_updated(task.id), data=workspace)

    @resultify
    def update_task_priority(
        self,
        user_id: str,
        todo_id: str,
        task_id: str,
        priority: int,
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        try:
            target_priority = Priority(priority)
        except ValueError:
            raise InvalidInputError(ToDoMessage.invalid_priority(priority))
        task = self.task_repo.update_task_priority(
            todo_id=valid_todo_id,
            task_id=task_id,
            priority=target_priority.value,
        )
        if task is None:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(ToDoMessage.task_updated(task.id), data=workspace)

    @resultify
    def update_task_due(
        self,
        user_id: str,
        todo_id: str,
        task_id: str,
        due: date | None,
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        task = self.task_repo.update_task_due(
            todo_id=valid_todo_id,
            task_id=task_id,
            due=due,
        )
        if task is None:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(ToDoMessage.task_updated(task.id), data=workspace)

    @resultify
    def update_task_order(
        self,
        user_id: str,
        todo_id: str,
        positions_by_task_id: dict[str, int],
    ) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        tasks = self.task_repo.update_task_order(
            todo_id=valid_todo_id,
            positions_by_task_id=positions_by_task_id,
        )
        if tasks is None:
            raise NotFoundError(ToDoMessage.tasks_not_found())
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(ToDoMessage.task_order_updated(), data=workspace)
