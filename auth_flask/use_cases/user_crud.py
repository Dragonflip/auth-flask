from auth_flask.entity.user import User
from auth_flask.adapters.interfaces.user_repository import UserRepo
from auth_flask.adapters.interfaces.hash import HashManager


class UserCrud:
    def __init__(self, repository: UserRepo, hash_manager: HashManager):
        self.repository = repository
        self.hash_manager = hash_manager

    def create_user(self, user_data: dict):
        user_dict = {
            'username': user_data['username'],
            'email': user_data['email'],
            'hashed_password': self.hash_manager.hash_password(
                user_data['password']
            ),
        }
        user = User(**user_dict)
        self.repository.save_user(user)

    def update_user(self, user_data: dict):
        user = User(**user_data)
        self.repository.save_user(user)

    def get_user_by_id(self, id: int):
        return self.repository.get_user_by_id(id)

    def delete_user_by_id(self, id: int):
        user = self.get_user_by_id(id)
        self.repository.delete_user(user)

    def list_users(self):
        return self.repository.list_users()
