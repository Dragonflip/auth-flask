from typing_extensions import TypedDict
from auth_flask.entity.token import Token
from datetime import datetime

Decoded = TypedDict('Decoded', {'usenamr': str, 'exp': int})


class TokenManager:
    def generate_token(
        self, username: str, expiration_time: datetime
    ) -> Token:
        error_string = f'Metodo ainda nao implementado para os parametros {user_id, expiration_time}'
        raise NotImplementedError(error_string)

    def decode_token(self, token: Token) -> Decoded:
        error_string = (
            f'Metodo ainda nao implementado para o parametro {token}'
        )
        raise NotImplementedError(error_string)
