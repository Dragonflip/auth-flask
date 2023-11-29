from typing import List
from auth_flask.entity.user import User


class UserRepo:
    def get_user_by_username(self, username: str) -> User:
        raise NotImplemented

    def delete_user(self, user: User) -> None:
        raise NotImplemented

    def save_user(self, user: User) -> None:
        raise NotImplemented

    def list_users(self) -> List[User]:
        raise NotImplemented

    def update_user(self, user: User) -> User:
        raise NotImplemented
