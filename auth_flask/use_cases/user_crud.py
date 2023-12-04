from auth_flask.entity.user import User
from auth_flask.adapters.interfaces.user_repository import UserRepo


class UserCrud:
    def __init__(self, repository: UserRepo):
        self.repository = repository

    def create_user(self, user: User):
        user_data = user.to_dict()
        return self.repository.create_user(user_data)

    def get_user_by_id(self, id: int):
        user_model = self.repository.get_user_by_id(id)
        user = User.from_dict(user_model.__dict__)
        return user

    def list_users(self):
        users_model = self.repository.list_users()
        return [User.from_dict(user.__dict__) for user in users_model]

    def delete_user_by_id(self, id: int):
        return self.repository.delete_user(id)

    def update_user(self, id: int, data: dict):
        if not self.repository.update_user(id, data):
            return False
        user = self.get_user_by_id(id)
        return user
