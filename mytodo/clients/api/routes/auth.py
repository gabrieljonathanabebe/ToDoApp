# mytodo/clients/api/routes/auth.py

from fastapi import APIRouter, Depends, status

from mytodo.clients.api import deps, http_results
from mytodo.clients.api.schemas.auth import LoginRequest, RegisterRequest, UserResponse
from mytodo.core.services import UserService
from mytodo.infra.adapters import UserAdapter


router = APIRouter()


@router.post("/login", response_model=UserResponse)
def login(
    body: LoginRequest, service: UserService = Depends(deps.get_user_service)
) -> UserResponse:
    res = service.authenticate(body.username, body.password)
    if res.ok and res.data is not None:
        return UserAdapter.domain_to_response(res.data)
    http_results.raise_http_error(res)


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register(
    body: RegisterRequest, service: UserService = Depends(deps.get_user_service)
) -> UserResponse:
    res = service.create_user(body.username, body.password)
    if res.ok and res.data is not None:
        return UserAdapter.domain_to_response(res.data)
    http_results.raise_http_error(res)
