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
def use_case(db_connection_handler):
    hash_manager = HashBcrypt()
    user_repo = DatabaseAdapter(db_connection_handler, hash_manager)
    use_case = UserCrud(user_repo)
    return use_case


@fixture
def user():
    user_dict = {
        'username': 'joao',
        'email': 'joao@email.com',
        'password': 'abc123',
    }
    user = User.from_dict(user_dict)
    return user


def test_create_user(user, use_case):
    assert use_case.create_user(user)


def test_list_all_users(user, use_case):
    use_case.create_user(user)
    users = use_case.list_users()
    assert len(users) == 1
    assert users[0].username == user.username


def test_get_by_id(user, use_case):
    use_case.create_user(user)
    new_user = use_case.get_user_by_id(1)
    assert new_user.username == user.username
    assert new_user.email == user.email


def test_delete_user(user, use_case):
    use_case.create_user(user)
    use_case.delete_user_by_id(1)
    users = use_case.list_users()
    assert len(users) == 0


def test_update_user(user, use_case):
    use_case.create_user(user)
    update = {'email': 'test@email.com'}
    new_user = use_case.update_user(1, update)
    assert new_user.email == update.get('email')


def test_update_password(user, use_case):
    hash_manager = HashBcrypt()
    use_case.create_user(user)
    new_password = 'empadao_frango'
    update = {'password': new_password}
    new_user = use_case.update_user(1, update)
    assert hash_manager.check_password(new_password, new_user.password)
