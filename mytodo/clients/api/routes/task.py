# mytodo/clients/api/routes/task.py

from fastapi import APIRouter, Depends, status

from mytodo.core.services import ToDoService, TaskService
from mytodo.infra.adapters import ToDoAdapter
from mytodo.domain import User

from mytodo.clients.api import deps, http_results
from mytodo.clients.api.schemas import (
    CreateTaskRequest,
    UpdateTaskStatusRequest,
    UpdateTaskDescriptionRequest,
    ToDoDetailResponse,
    ToDoWorkspaceResponse,
    UpdateTaskPriorityRequest,
    UpdateTaskDueRequest,
    UpdateTaskOrderRequest,
)


router = APIRouter()


@router.get("", response_model=ToDoDetailResponse)
def get_todo_detail(
    todo_id: str,
    user: User = Depends(deps.get_current_user),
    service: ToDoService = Depends(deps.get_todo_service),
) -> ToDoDetailResponse:
    result = service.get_todo_detail(user.id, todo_id)
    detail = http_results.unwrap_result(result)
    return ToDoAdapter.detail_domain_to_response(detail)


@router.post(
    "/tasks",
    response_model=ToDoWorkspaceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    todo_id: str,
    body: CreateTaskRequest,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    result = service.create_task(
        user_id=user.id,
        todo_id=todo_id,
        description=body.description,
        priority=body.priority.value,
        due=body.due,
        notes=body.notes,
    )
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.delete(
    "/tasks/{task_id}",
    response_model=ToDoWorkspaceResponse,
    status_code=status.HTTP_200_OK,
)
def delete_task(
    todo_id: str,
    task_id: str,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    result = service.delete_task(user.id, todo_id, task_id)
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.patch("/tasks/{task_id}/status", response_model=ToDoWorkspaceResponse)
def update_task_status(
    todo_id: str,
    task_id: str,
    body: UpdateTaskStatusRequest,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    result = service.update_task_status(
        user_id=user.id,
        todo_id=todo_id,
        task_id=task_id,
        status=body.status.value,
    )
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.patch("/tasks/{task_id}/description", response_model=ToDoWorkspaceResponse)
def update_task_description(
    todo_id: str,
    task_id: str,
    body: UpdateTaskDescriptionRequest,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    result = service.update_task_description(
        user_id=user.id,
        todo_id=todo_id,
        task_id=task_id,
        description=body.description,
    )
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.patch("/tasks/{task_id}/priority", response_model=ToDoWorkspaceResponse)
def update_task_priority(
    todo_id: str,
    task_id: str,
    body: UpdateTaskPriorityRequest,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    result = service.update_task_priority(
        user_id=user.id,
        todo_id=todo_id,
        task_id=task_id,
        priority=body.priority,
    )
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.patch("/tasks/{task_id}/due", response_model=ToDoWorkspaceResponse)
def update_task_due(
    todo_id: str,
    task_id: str,
    body: UpdateTaskDueRequest,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    result = service.update_task_due(
        user_id=user.id,
        todo_id=todo_id,
        task_id=task_id,
        due=body.due,
    )
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.patch("/tasks/order", response_model=ToDoWorkspaceResponse)
def update_task_order(
    todo_id: str,
    body: UpdateTaskOrderRequest,
    user: User = Depends(deps.get_current_user),
    service: TaskService = Depends(deps.get_task_service),
) -> ToDoWorkspaceResponse:
    positions_by_task_id = {item.id: item.position for item in body.items}
    result = service.update_task_order(
        user_id=user.id,
        todo_id=todo_id,
        positions_by_task_id=positions_by_task_id,
    )
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)
