# mytodo/core/services/user.py

from uuid import uuid4

from mytodo.core.results import Code, Result
from mytodo.core.errors import AlreadyExistsError, UnauthorizedError
from mytodo.core.messages import ToDoMessage
from mytodo.core.responses import Success, created, ok, resultify
from mytodo.domain import User
from mytodo.infra.repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def _normalize_username(self, username: str) -> str:
        return username.strip().lower()

    def get_users(self) -> Result[list[User]]:
        return Result(Code.OK, data=self.user_repo.get_users())

    def get_user(self, username: str) -> User | None:
        username = self._normalize_username(username)
        return self.user_repo.get_by_username(username)

    @resultify
    def authenticate(self, username: str, password: str) -> Success[User]:
        username = self._normalize_username(username)
        user = self.user_repo.get_by_username(username)
        if user is None or user.password != password:
            raise UnauthorizedError(ToDoMessage.invalid_credentials())
        return ok(ToDoMessage.welcome_user(user.username), data=user)

    @resultify
    def create_user(self, username: str, password: str) -> Success[User]:
        username = self._normalize_username(username)
        existing_user = self.user_repo.get_by_username(username)
        if existing_user is not None:
            raise AlreadyExistsError(
                ToDoMessage.username_already_exists(existing_user.username)
            )
        user = User(id=str(uuid4()), username=username, password=password)
        created_user = self.user_repo.create_user(user)
        return created(
            ToDoMessage.user_created(created_user.username), data=created_user
        )
