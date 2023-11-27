from auth_flask.entity.user import User


def test_user_from_dict():
    init_dict = {
        'username': 'joao',
        'email': 'joao@email.com',
        'password': 'abc123',
    }
    user = User.from_dict(init_dict)
    assert user.username == init_dict['username']
    assert user.email == init_dict['email']
    assert user.password == init_dict['password']


def test_user_to_dict():
    init_dict = {
        'username': 'joao',
        'email': 'joao@email.com',
        'password': 'abc123',
    }
    user = User.from_dict(init_dict)
    assert user.to_dict() == init_dict
