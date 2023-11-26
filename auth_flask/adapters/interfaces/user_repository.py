from typing import List
from entity.user import User


class UserRepo:
    def get_user_by_id(self, id: int) -> User:
        raise NotImplemented

    def delete_user(self, user: User) -> None:
        raise NotImplemented

    def save_user(self, user: User) -> None:
        raise NotImplemented

    def list_users(self) -> List[User]:
        raise NotImplemented
