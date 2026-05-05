# mytodo/infra/adapters/task_adapter.py

from mytodo.domain import Task
from mytodo.infra.db.models import TaskModel
from mytodo.clients.api.schemas import TaskResponse


class TaskAdapter:
    @staticmethod
    def model_to_domain(model: TaskModel) -> Task:
        return Task(
            id=model.id,
            position=model.position,
            description=model.description,
            priority=model.priority,
            status=model.status,
            due=model.due,
            created_at=model.created_at,
            updated_at=model.updated_at,
            completed_at=model.completed_at,
            notes=model.notes,
        )

    @staticmethod
    def models_to_domain(models: list[TaskModel]) -> list[Task]:
        return [TaskAdapter.model_to_domain(model) for model in models]

    @staticmethod
    def domain_to_response(task: Task) -> TaskResponse:
        return TaskResponse(
            id=task.id,
            position=task.position,
            description=task.description,
            priority=task.priority.name,
            status=task.status.value,
            due=task.due,
            days_left=task.days_left,
            created_at=task.created_at,
            updated_at=task.updated_at,
            completed_at=task.completed_at,
            notes=task.notes,
            lead_time_seconds=task.lead_time_seconds,
        )

    @staticmethod
    def domains_to_response(tasks: list[Task]) -> list[TaskResponse]:
        return [TaskAdapter.domain_to_response(task) for task in tasks]
