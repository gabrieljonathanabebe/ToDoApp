# mytodo/core/services/base.py

from mytodo.core.errors import InvalidInputError, NotFoundError
from mytodo.core.messages import ToDoMessage
from mytodo.infra.repositories import ToDoRepository


class BaseService:
    def __init__(self, todo_repo: ToDoRepository | None = None):
        self.todo_repo = todo_repo

    def require_todo_id(self, user_id: str, todo_id: str) -> str:
        if self.todo_repo is None:
            raise RuntimeError("todo_repo is required for todo checks")
        valid_todo_id = self.todo_repo.get_todo_id(user_id, todo_id)
        if valid_todo_id is None:
            raise NotFoundError(ToDoMessage.todo_not_found())
        return valid_todo_id
