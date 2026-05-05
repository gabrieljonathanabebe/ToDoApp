# mytodo/clients/api/schemas/task.py

from datetime import date, datetime
from pydantic import BaseModel

from mytodo.domain import Priority, Status


# ===== REQUESTS ==============================================================
class CreateTaskRequest(BaseModel):
    description: str
    priority: Priority
    due: date | None = None
    notes: str | None = None


class UpdateTaskStatusRequest(BaseModel):
    status: Status


class UpdateTaskDescriptionRequest(BaseModel):
    description: str


class UpdateTaskPriorityRequest(BaseModel):
    priority: int


class UpdateTaskDueRequest(BaseModel):
    due: date | None = None


class TaskOrderItemRequest(BaseModel):
    id: str
    position: int


class UpdateTaskOrderRequest(BaseModel):
    items: list[TaskOrderItemRequest]


# ===== RESPONSES =============================================================
class TaskResponse(BaseModel):
    id: str
    position: int
    description: str
    priority: str
    status: str
    due: date | None = None
    days_left: int | None = None
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None = None
    notes: str | None
    lead_time_seconds: int | None = None


class ToDoDetailResponse(BaseModel):
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
    tasks: list[TaskResponse]
