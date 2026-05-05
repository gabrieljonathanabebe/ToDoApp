# mytodo/clients/api/schemas/__init__.py

from mytodo.clients.api.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    UserResponse,
)
from mytodo.clients.api.schemas.todo import (
    CreateToDoRequest,
    ToDoSummaryResponse,
    ToDoWorkspaceResponse,
    ToDoWorkspaceStatsResponse,
)
from mytodo.clients.api.schemas.task import (
    CreateTaskRequest,
    UpdateTaskStatusRequest,
    UpdateTaskDescriptionRequest,
    UpdateTaskPriorityRequest,
    UpdateTaskDueRequest,
    UpdateTaskOrderRequest,
    TaskResponse,
    ToDoDetailResponse,
)


__all__ = [
    "LoginRequest",
    "RegisterRequest",
    "UserResponse",
    "CreateToDoRequest",
    "ToDoSummaryResponse",
    "CreateTaskRequest",
    "UpdateTaskStatusRequest",
    "UpdateTaskDescriptionRequest",
    "UpdateTaskPriorityRequest",
    "UpdateTaskDueRequest",
    "UpdateTaskOrderRequest",
    "TaskResponse",
    "ToDoDetailResponse",
    "ToDoWorkspaceResponse",
    "ToDoWorkspaceStatsResponse",
]
