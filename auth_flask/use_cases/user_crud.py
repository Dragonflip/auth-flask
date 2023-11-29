from auth_flask.entity.user import User
from auth_flask.adapters.interfaces.user_repository import UserRepo


class UserCrud:
    def __init__(self, repository: UserRepo):
        self.repository = repository

    def create_user(self, user: User):
        self.repository.save_user(user)

    def update_user(self, user: User):
        user = self.repository.update_user(user)
        return user

    def get_user_by_username(self, username: str):
        return self.repository.get_user_by_username(username)

    def delete_user_by_username(self, username: str):
        user = self.get_user_by_username(username)
        self.repository.delete_user(user)

    def list_users(self):
        return self.repository.list_users()
