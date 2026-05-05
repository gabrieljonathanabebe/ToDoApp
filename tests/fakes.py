from datetime import datetime, timezone
from uuid import uuid4

from mytodo.domain import ToDoDetail, ToDoWorkspace


class FakeToDoRepo:
    def __init__(self):
        self.workspaces_by_user_id: dict[str, ToDoWorkspace] = {}

    def get_todo_id(self, user_id: str, todo_id: str) -> str | None:
        workspace = self.get_workspace(user_id)
        return next((todo.id for todo in workspace.todos if todo.id == todo_id), None)

    def get_workspace(self, user_id: str) -> ToDoWorkspace:
        return self.workspaces_by_user_id.setdefault(
            user_id,
            ToDoWorkspace(todos=[]),
        )

    def get_todo_detail(self, user_id: str, todo_id: str) -> ToDoDetail | None:
        workspace = self.get_workspace(user_id)
        return next((todo for todo in workspace.todos if todo.id == todo_id), None)

    def create_todo(self, user_id: str, title: str) -> ToDoDetail:
        workspace = self.get_workspace(user_id)
        now = datetime.now(timezone.utc)
        todo = ToDoDetail(
            id=str(uuid4()),
            title=title,
            position=len(workspace.todos) + 1,
            tasks=[],
            created_at=now,
            updated_at=now,
        )
        workspace.todos.append(todo)
        return todo

    def delete_todo(self, user_id: str, todo_id: str) -> bool:
        workspace = self.get_workspace(user_id)
        original_count = len(workspace.todos)
        workspace.todos = [todo for todo in workspace.todos if todo.id != todo_id]
        return len(workspace.todos) != original_count


FakeRepo = FakeToDoRepo
