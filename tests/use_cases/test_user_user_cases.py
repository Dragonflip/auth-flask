# extern library
from pytest import fixture

# entity
from auth_flask.entity.user import User

# use cases
from auth_flask.use_cases.user_crud import UserCrud

# adapters
from auth_flask.adapters.hash.hash_password import HashBcrypt
from auth_flask.adapters.database.user_repository import DatabaseAdapter

# frameworks
from auth_flask.frameworks.database.config.connection import (
    DBConnectionHandler,
)
from auth_flask.frameworks.database.config.base import Base


@fixture()
def db_connection_handler():

    conn_handler = DBConnectionHandler()
    conn_handler.__connection_string = 'sqlite:///test.db'
    conn_handler.__engine = conn_handler.create_engine()
    Base.metadata.create_all(conn_handler.get_engine())

    yield conn_handler

    Base.metadata.drop_all(conn_handler.get_engine())


@fixture
def user():
    user_dict = {
        'username': 'joao',
        'email': 'joao@email.com',
        'password': 'abc123',
    }
    user = User.from_dict(user_dict)
    return user


def test_list_user(user, db_connection_handler):
    hash_manager = HashBcrypt()
    user_repo = DatabaseAdapter(db_connection_handler, hash_manager)
    caso_uso_user = UserCrud(user_repo)

    caso_uso_user.create_user(user)
    users = caso_uso_user.list_users()

    assert len(users) == 1
    assert users[0].username == user.username
    assert users[0].email == user.email


def test_delete_user(user, db_connection_handler):
    hash_manager = HashBcrypt()
    user_repo = DatabaseAdapter(db_connection_handler, hash_manager)
    caso_uso_user = UserCrud(user_repo)

    caso_uso_user.create_user(user)
    caso_uso_user.delete_user_by_username(user.username)
    users = caso_uso_user.list_users()

    assert len(users) == 0


def test_update_user(user, db_connection_handler):
    hash_manager = HashBcrypt()
    user_repo = DatabaseAdapter(db_connection_handler, hash_manager)
    caso_uso_user = UserCrud(user_repo)

    caso_uso_user.create_user(user)
    user.email = 'jp@email.com'
    caso_uso_user.update_user(user)
    user_from_db = caso_uso_user.get_user_by_username(user.username)

    assert user_from_db.username == user.username
    assert user_from_db.email == user.email
