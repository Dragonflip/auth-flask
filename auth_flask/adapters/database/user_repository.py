# entity imports
from auth_flask.entity.user import User

# adapter imports
from auth_flask.adapters.interfaces.hash import HashManager
from auth_flask.adapters.interfaces.user_repository import UserRepo

# frameworks imports
from auth_flask.frameworks.database.config.connection import (
    DBConnectionHandler,
)
from auth_flask.frameworks.database.models.user_model import UserModel


class DatabaseAdapter(UserRepo):
    def __init__(
        self,
        connection_handler: DBConnectionHandler,
        hash_adapter: HashManager,
    ):
        self.connection_handle = connection_handler
        self.hash_adapter = hash_adapter

    def create_user(self, data: dict):
        with DBConnectionHandler() as db:
            password = data.get('password')
            if password and isinstance(password, str):
                data['password'] = self.hash_adapter.hash_password(password)
            if db.session:
                user_model = UserModel(**data)
                db.session.add(user_model)
                db.session.commit()
                return True
            return False

    def delete_user(self, id: int):
        with DBConnectionHandler() as db:
            if db.session:
                db.session.query(UserModel).filter(
                    UserModel.user_id == id
                ).delete()
                db.session.commit()
                return True
            return False

    def list_users(self):
        with DBConnectionHandler() as db:
            if db.session:
                user_rows = db.session.query(UserModel).all()
                users = [user for user in user_rows]
                return users

    def get_user_by_username(self, username: str):
        with DBConnectionHandler() as db:
            if db.session:
                user = (
                    db.session.query(UserModel)
                    .filter(UserModel.username == username)
                    .one()
                )
                return user

    def get_user_by_id(self, id: int):
        with DBConnectionHandler() as db:
            if db.session:
                user = (
                    db.session.query(UserModel)
                    .filter(UserModel.user_id == id)
                    .one()
                )
                return user

    def update_user(self, id: int, data: dict):
        with DBConnectionHandler() as db:
            password = data.get('password')
            if password and isinstance(password, str):
                data['password'] = self.hash_adapter.hash_password(password)
            if db.session:
                db.session.query(UserModel).filter(
                    UserModel.user_id == id
                ).update(data)
                db.session.commit()
                return True
            return False
