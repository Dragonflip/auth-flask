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

    def save_user(self, user: User) -> None:
        with DBConnectionHandler() as db:
            if isinstance(user.password, str):
                user.password = self.hash_adapter.hash_password(user.password)
            user_model = UserModel(**user.__dict__)
            db.session.add(user_model)
            db.session.commit()

    def update_user(self, user: User):
        with DBConnectionHandler() as db:
            if isinstance(user.password, str):
                user.password = self.hash_adapter.hash_password(user.password)
            user = (
                db.session.query(UserModel)
                .filter(UserModel.username == user.username)
                .update(
                    {
                        'username': user.username,
                        'email': user.email,
                        'password': user.password,
                    }
                )
            )
            db.session.commit()
            return user

    def list_users(self):
        with DBConnectionHandler() as db:
            user_rows = db.session.query(UserModel).all()
            users = [
                User(user.username, user.password, user.email)
                for user in user_rows
            ]
            return users

    def get_user_by_username(self, username: str):
        with DBConnectionHandler() as db:
            user = (
                db.session.query(UserModel)
                .filter(UserModel.username == username)
                .one()
            )
            return user

    def delete_user(self, user: User):
        with DBConnectionHandler() as db:
            db.session.query(UserModel).filter(
                UserModel.username == user.username
            ).delete()
            db.session.commit()
