# mytodo/infra/adapters/todo_adapter.py

from mytodo.domain import ToDoWorkspace, ToDoWorkspaceStats, ToDoSummary, ToDoDetail
from mytodo.infra.adapters import TaskAdapter
from mytodo.infra.db.models import TaskModel, ToDoModel
from mytodo.clients.api.schemas import (
    ToDoSummaryResponse,
    ToDoDetailResponse,
    ToDoWorkspaceResponse,
    ToDoWorkspaceStatsResponse,
)


class ToDoAdapter:
    @staticmethod
    def orm_to_detail_domain(
        todo_orm: ToDoModel, task_orms: list[TaskModel]
    ) -> ToDoDetail:
        return ToDoDetail(
            id=todo_orm.id,
            title=todo_orm.title,
            position=todo_orm.position,
            tasks=TaskAdapter.models_to_domain(task_orms),
            created_at=todo_orm.created_at,
            updated_at=todo_orm.updated_at,
        )

    @staticmethod
    def orms_to_workspace_domain(
        todo_orms: list[ToDoModel], task_orms_by_todo_id: dict[str, list[TaskModel]]
    ) -> ToDoWorkspace:
        todos = [
            ToDoAdapter.orm_to_detail_domain(
                todo_orm=todo_orm, task_orms=task_orms_by_todo_id.get(todo_orm.id, [])
            )
            for todo_orm in todo_orms
        ]
        return ToDoWorkspace(todos=todos)

    @staticmethod
    def summary_domain_to_response(
        summary: ToDoSummary,
    ) -> ToDoSummaryResponse:
        return ToDoSummaryResponse(
            id=summary.id,
            title=summary.title,
            position=summary.position,
            task_count=summary.task_count,
            open_task_count=summary.open_task_count,
            done_task_count=summary.done_task_count,
            overdue_task_count=summary.overdue_task_count,
            completion_rate=summary.completion_rate,
            created_at=summary.created_at,
            updated_at=summary.updated_at,
        )

    @staticmethod
    def detail_domain_to_response(detail: ToDoDetail) -> ToDoDetailResponse:
        return ToDoDetailResponse(
            id=detail.id,
            title=detail.title,
            position=detail.position,
            task_count=detail.task_count,
            open_task_count=detail.open_task_count,
            done_task_count=detail.done_task_count,
            overdue_task_count=detail.overdue_task_count,
            completion_rate=detail.completion_rate,
            created_at=detail.created_at,
            updated_at=detail.updated_at,
            tasks=TaskAdapter.domains_to_response(detail.tasks),
        )

    @staticmethod
    def workspace_stats_domain_to_response(
        stats: ToDoWorkspaceStats,
    ) -> ToDoWorkspaceStatsResponse:
        return ToDoWorkspaceStatsResponse(
            todo_count=stats.todo_count,
            total_task_count=stats.total_task_count,
            total_open_task_count=stats.total_open_task_count,
            total_done_task_count=stats.total_done_task_count,
            total_overdue_task_count=stats.total_overdue_task_count,
            overall_completion_rate=stats.overall_completion_rate,
        )

    @staticmethod
    def workspace_domain_to_response(workspace: ToDoWorkspace) -> ToDoWorkspaceResponse:
        todo_summaries = [
            ToDoAdapter.summary_domain_to_response(summary)
            for summary in workspace.todo_summaries
        ]
        todos = [
            ToDoAdapter.detail_domain_to_response(todo) for todo in workspace.todos
        ]
        stats = ToDoAdapter.workspace_stats_domain_to_response(workspace.stats)
        return ToDoWorkspaceResponse(
            todo_summaries=todo_summaries, todos=todos, stats=stats
        )
