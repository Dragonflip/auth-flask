from auth_flask.entity.user import User


def test_user_from_dict():
    init_dict = {
        'first_name': 'joao',
        'last_name': 'marques',
        'email': 'jpmarques@as.com',
    }
    user = User.from_dict(init_dict)
    assert user.first_name == init_dict['first_name']
    assert user.last_name == init_dict['last_name']
    assert user.email == init_dict['email']


def test_user_to_dict():
    init_dict = {
        'first_name': 'joao',
        'last_name': 'marques',
        'email': 'jpmarques@as.com',
    }
    user = User.from_dict(init_dict)
    assert user.to_dict() == init_dict
