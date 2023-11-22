from auth_flask.entity.token import Token, Claim
from datetime import datetime


class TokenManager:
    def generate_token(self, user_id: int, expiration_time: datetime) -> Token:
        error_string = f'Metodo ainda nao implementado para os parametros {user_id, expiration_time}'
        raise NotImplementedError(error_string)

    def validate_token(self, token: Token) -> Claim:
        error_string = (
            f'Metodo ainda nao implementado para o parametro {token}'
        )
        raise NotImplementedError(error_string)
