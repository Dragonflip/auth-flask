from auth_flask.entity.user import User


class UserSerializer:
    @staticmethod
    def serialize(user: User):
        return {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
        }
