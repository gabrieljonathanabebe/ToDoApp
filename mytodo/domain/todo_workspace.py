# mytodo/domain/todo_workspace.py

from pydantic import BaseModel

from mytodo.domain.todo_detail import ToDoDetail
from mytodo.domain.todo_summary import ToDoSummary


class ToDoWorkspaceStats(BaseModel):
    todo_count: int
    total_task_count: int
    total_open_task_count: int
    total_done_task_count: int
    total_overdue_task_count: int
    overall_completion_rate: float


class ToDoWorkspace(BaseModel):
    todos: list[ToDoDetail]

    @property
    def todo_summaries(self) -> list[ToDoSummary]:
        return [todo.summary for todo in self.todos]

    @property
    def stats(self) -> ToDoWorkspaceStats:
        summaries = self.todo_summaries
        total_task_count = sum(summary.task_count for summary in summaries)
        total_done_task_count = sum(summary.done_task_count for summary in summaries)
        return ToDoWorkspaceStats(
            todo_count=len(summaries),
            total_task_count=total_task_count,
            total_open_task_count=sum(summary.open_task_count for summary in summaries),
            total_done_task_count=total_done_task_count,
            total_overdue_task_count=sum(
                summary.overdue_task_count for summary in summaries
            ),
            overall_completion_rate=(
                0.0
                if total_task_count == 0
                else total_done_task_count / total_task_count
            ),
        )
