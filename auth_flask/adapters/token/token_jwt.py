from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from auth_flask.adapters.interfaces.token_manager import TokenManager
from auth_flask.entity.token import Token


SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'


class TokenJWT(TokenManager):
    def __init__(self):
        self.__secret_key = SECRET_KEY
        self.__algorithm = ALGORITHM

    def generate_token(self, username, expiration_time):
        to_encode = {'username': username, 'exp': expiration_time}
        encoded_jwt = jwt.encode(
            to_encode, self.__secret_key, algorithm=self.__algorithm
        )
        token = Token(
            token_value=encoded_jwt,
            expires_at=expiration_time,
            username=username,
        )
        return token

    def decode_token(self, token: str):
        try:
            decoded_value = jwt.decode(
                token,
                self.__secret_key,
                algorithms=[self.__algorithm],
            )
            return decoded_value
        except ExpiredSignatureError:
            return False
        except JWTError:
            return False
