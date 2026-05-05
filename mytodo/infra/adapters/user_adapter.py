# mytodo/infra/adapters/user_adapter.py

from mytodo.domain import User
from mytodo.infra.db.models import UserModel
from mytodo.clients.api.schemas import UserResponse


class UserAdapter:
    @staticmethod
    def model_to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            username=model.username,
            password=model.password,
            created_at=model.created_at,
        )

    @staticmethod
    def domain_to_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            username=user.username,
            password=user.password,
            created_at=user.created_at,
        )

    @staticmethod
    def domain_to_response(user: User) -> UserResponse:
        return UserResponse(
            id=user.id,
            username=user.username,
        )
