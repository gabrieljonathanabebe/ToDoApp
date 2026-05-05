# mytodo/core/services/todo.py

from mytodo.core.services import BaseService
from mytodo.core.errors import AlreadyExistsError, NotFoundError
from mytodo.core.messages import ToDoMessage
from mytodo.core.responses import Success, created, ok, resultify
from mytodo.domain import ToDoDetail, ToDoSummary, ToDoWorkspace
from mytodo.infra.repositories import ToDoRepository


class ToDoService(BaseService):
    def __init__(
        self,
        todo_repo: ToDoRepository,
    ):
        super().__init__(todo_repo=todo_repo)
        self.todo_repo = todo_repo

    @resultify
    def get_workspace(self, user_id: str) -> Success[ToDoWorkspace]:
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(data=workspace)

    @resultify
    def get_todo_summaries(self, user_id: str) -> Success[list[ToDoSummary]]:
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(data=workspace.todo_summaries)

    @resultify
    def create_todo(self, user_id: str, title: str) -> Success[ToDoWorkspace]:
        existing_todos = self.todo_repo.get_workspace(user_id).todo_summaries
        if any(todo.title == title for todo in existing_todos):
            raise AlreadyExistsError(ToDoMessage.todo_already_exists(title))
        self.todo_repo.create_todo(user_id, title)
        workspace = self.todo_repo.get_workspace(user_id)
        return created(ToDoMessage.todo_created(title), data=workspace)

    @resultify
    def delete_todo(self, user_id: str, todo_id: str) -> Success[ToDoWorkspace]:
        valid_todo_id = self.require_todo_id(user_id, todo_id)
        is_deleted = self.todo_repo.delete_todo(user_id, valid_todo_id)
        if not is_deleted:
            raise NotFoundError(ToDoMessage.todo_not_found())
        workspace = self.todo_repo.get_workspace(user_id)
        return ok(ToDoMessage.todo_deleted(), data=workspace)

    @resultify
    def get_todo_detail(
        self,
        user_id: str,
        todo_id: str,
    ) -> Success[ToDoDetail]:
        detail = self.todo_repo.get_todo_detail(user_id, todo_id)
        if detail is None:
            raise NotFoundError(ToDoMessage.todo_not_found())
        return ok(data=detail)
