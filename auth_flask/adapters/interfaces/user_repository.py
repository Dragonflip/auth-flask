from typing import List
from auth_flask.entity.user import User


class UserRepo:
    def get_user_by_id(self, id: int) -> User:
        raise NotImplemented

    def get_user_by_username(self, username: str) -> User:
        raise NotImplemented

    def delete_user(self, id: int) -> None:
        raise NotImplemented

    def create_user(self, data: dict) -> None:
        raise NotImplemented

    def list_users(self) -> List[User]:
        raise NotImplemented

    def update_user(self, id: int, data: dict) -> User:
        raise NotImplemented
