# mytodo/domain/todo_summary.py

from datetime import datetime

from pydantic import BaseModel


class ToDoSummary(BaseModel):
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
