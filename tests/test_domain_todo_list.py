from datetime import datetime, timezone

from mytodo.domain import Status, ToDoDetail, ToDoWorkspace
import tests.factories as factories


def test_todo_detail_exposes_summary_counts() -> None:
    now = datetime.now(timezone.utc)
    todo = ToDoDetail(
        id="todo-id",
        title="Project",
        position=1,
        tasks=[
            factories.make_task(status=Status.open),
            factories.make_task(status=Status.done),
        ],
        created_at=now,
        updated_at=now,
    )

    summary = todo.summary

    assert todo.task_count == 2
    assert todo.open_task_count == 1
    assert todo.done_task_count == 1
    assert todo.completion_rate == 0.5
    assert summary.id == todo.id
    assert summary.title == todo.title


def test_workspace_stats_aggregate_todos() -> None:
    now = datetime.now(timezone.utc)
    workspace = ToDoWorkspace(
        todos=[
            ToDoDetail(
                id="first",
                title="First",
                position=1,
                tasks=[
                    factories.make_task(status=Status.done),
                    factories.make_task(status=Status.open),
                ],
                created_at=now,
                updated_at=now,
            ),
            ToDoDetail(
                id="second",
                title="Second",
                position=2,
                tasks=[factories.make_task(status=Status.done)],
                created_at=now,
                updated_at=now,
            ),
        ]
    )

    assert len(workspace.todo_summaries) == 2
    assert workspace.stats.todo_count == 2
    assert workspace.stats.total_task_count == 3
    assert workspace.stats.total_open_task_count == 1
    assert workspace.stats.total_done_task_count == 2
    assert workspace.stats.overall_completion_rate == 2 / 3


def test_empty_workspace_has_zero_stats() -> None:
    workspace = ToDoWorkspace(todos=[])

    assert workspace.todo_summaries == []
    assert workspace.stats.todo_count == 0
    assert workspace.stats.total_task_count == 0
    assert workspace.stats.overall_completion_rate == 0.0
