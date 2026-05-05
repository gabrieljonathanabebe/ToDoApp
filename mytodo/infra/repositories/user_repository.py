# mytodo/infra/repositories/user_repository.py

from sqlalchemy import select

from mytodo.domain import User
from mytodo.infra.adapters import UserAdapter
from mytodo.infra.db.models import UserModel
from mytodo.infra.repositories import BaseRepository


class UserRepository(BaseRepository):
    def get_users(self) -> list[User]:
        stmt = select(UserModel).order_by(UserModel.username.asc())
        user_models = self.db.execute(stmt).scalars().all()
        return [UserAdapter.model_to_domain(user_model) for user_model in user_models]

    def get_by_username(self, username: str) -> User | None:
        user_model = self._get_user_model_by_username(username)
        if user_model is None:
            return None
        return UserAdapter.model_to_domain(user_model)

    def create_user(self, user: User) -> User:
        user_model = UserAdapter.domain_to_model(user)
        self._commit_create(user_model)
        return UserAdapter.model_to_domain(user_model)
