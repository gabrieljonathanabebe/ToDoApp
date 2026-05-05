# mytodo/domain/todo_detail.py

from datetime import datetime

from pydantic import BaseModel

from mytodo.domain.task import Status, Task
from mytodo.domain.todo_summary import ToDoSummary


class ToDoDetail(BaseModel):
    id: str
    title: str
    position: int
    tasks: list[Task]
    created_at: datetime
    updated_at: datetime

    @property
    def task_count(self) -> int:
        return len(self.tasks)

    @property
    def open_task_count(self) -> int:
        return sum(task.status == Status.open for task in self.tasks)

    @property
    def done_task_count(self) -> int:
        return sum(task.status == Status.done for task in self.tasks)

    @property
    def overdue_task_count(self) -> int:
        return sum(
            task.days_left is not None
            and task.days_left < 0
            and task.status != Status.done
            for task in self.tasks
        )

    @property
    def completion_rate(self) -> float:
        if self.task_count == 0:
            return 0.0
        return self.done_task_count / self.task_count

    @property
    def summary(self) -> ToDoSummary:
        return ToDoSummary(
            id=self.id,
            title=self.title,
            position=self.position,
            task_count=self.task_count,
            open_task_count=self.open_task_count,
            done_task_count=self.done_task_count,
            overdue_task_count=self.overdue_task_count,
            completion_rate=self.completion_rate,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
