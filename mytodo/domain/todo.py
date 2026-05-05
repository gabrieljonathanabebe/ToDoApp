# mytodo/domain/todo.py

from mytodo.domain.todo_detail import ToDoDetail
from mytodo.domain.todo_summary import ToDoSummary
from mytodo.domain.todo_workspace import ToDoWorkspace, ToDoWorkspaceStats


ToDoOverview = ToDoSummary
Workspace = ToDoWorkspace
WorkspaceStats = ToDoWorkspaceStats


__all__ = [
    "ToDoDetail",
    "ToDoSummary",
    "ToDoOverview",
    "ToDoWorkspace",
    "ToDoWorkspaceStats",
    "Workspace",
    "WorkspaceStats",
]
