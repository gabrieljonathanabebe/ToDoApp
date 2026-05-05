# mytodo/clients/api/schemas/todo.py

from datetime import datetime
from pydantic import BaseModel

from mytodo.clients.api.schemas.task import ToDoDetailResponse


# ===== REQUESTS ==============================================================
class CreateToDoRequest(BaseModel):
    title: str


# ===== RESPONSES =============================================================
class ToDoSummaryResponse(BaseModel):
    id: str
    title: str
    position: int
    task_count: int
    open_task_count: int
    done_task_count: int
    overdue_task_count: int
    completion_rate: float
    created_at: datetime
    updated_at: datetime


class ToDoWorkspaceStatsResponse(BaseModel):
    todo_count: int
    total_task_count: int
    total_open_task_count: int
    total_done_task_count: int
    total_overdue_task_count: int
    overall_completion_rate: float


class ToDoWorkspaceResponse(BaseModel):
    todo_summaries: list[ToDoSummaryResponse]
    todos: list[ToDoDetailResponse]
    stats: ToDoWorkspaceStatsResponse
