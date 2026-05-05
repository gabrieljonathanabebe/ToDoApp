# mytodo/clients/api/routes/todo.py

from fastapi import APIRouter, Depends, status

from mytodo.infra.adapters import ToDoAdapter
from mytodo.core.services.todo import ToDoService
from mytodo.clients.api.schemas import ToDoSummaryResponse, ToDoWorkspaceResponse
from mytodo.clients.api import deps
import mytodo.clients.api.http_results as http_results
from mytodo.clients.api.schemas import CreateToDoRequest
from mytodo.domain import User


router = APIRouter()


@router.get("", response_model=list[ToDoSummaryResponse])
def get_todos(
    user: User = Depends(deps.get_current_user),
    service: ToDoService = Depends(deps.get_todo_service),
) -> list[ToDoSummaryResponse]:
    result = service.get_todo_summaries(user.id)
    summaries = http_results.unwrap_result(result)
    return [ToDoAdapter.summary_domain_to_response(summary) for summary in summaries]


@router.post(
    "", response_model=ToDoWorkspaceResponse, status_code=status.HTTP_201_CREATED
)
def create_todo(
    body: CreateToDoRequest,
    user: User = Depends(deps.get_current_user),
    service: ToDoService = Depends(deps.get_todo_service),
) -> ToDoWorkspaceResponse:
    result = service.create_todo(user_id=user.id, title=body.title)
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)


@router.delete(
    "/{todo_id}",
    response_model=ToDoWorkspaceResponse,
    status_code=status.HTTP_200_OK,
)
def delete_todo(
    todo_id: str,
    user: User = Depends(deps.get_current_user),
    service: ToDoService = Depends(deps.get_todo_service),
) -> ToDoWorkspaceResponse:
    result = service.delete_todo(user_id=user.id, todo_id=todo_id)
    workspace = http_results.unwrap_result(result)
    return ToDoAdapter.workspace_domain_to_response(workspace)
