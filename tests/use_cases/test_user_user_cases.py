from pytest import fixture
from auth_flask.entity.user import User
from auth_flask.repository.user import MemRepo
from auth_flask.use_cases.user import create_user, delete_user, update_user


@fixture
def user():
    init_dict = {
        'first_name': 'joao',
        'last_name': 'marques',
        'email': 'jpmarques@as.com',
    }
    user = User.from_dict(init_dict)
    return user


def test_list_users(user):
    repo = MemRepo([user.to_dict()])

    users = repo.list()

    assert len(users) == 1
    assert users[0].email == user.email


def test_create_user(user):
    repo = MemRepo()
    create_user(repo, user)

    users = repo.list()

    assert len(users) == 1
    assert users[0].email == user.email


def test_delete_user(user):
    repo = MemRepo()
    create_user(repo, user)
    delete_user(repo, user)

    users = repo.list()
    assert len(users) == 0


def test_update_user(user):
    repo = MemRepo()
    create_user(repo, user)

    user.first_name = 'paulo'
    user.last_name = 'macedes'
    update_user(repo, user)

    users = repo.list()
    assert len(users) == 1
    assert users[0].first_name == user.first_name
    assert users[0].last_name == user.last_name
