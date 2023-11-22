from auth_flask.entity.token import Token, Claim
from auth_flask.adapters.interfaces.token_manager import TokenManager
from auth_flask.adapters.interfaces.user_repository import UserRepo
from datetime import timedelta, datetime
from typing import Optional


class Authentication:
    def __init__(self, repository: UserRepo, token_manager: TokenManager):
        self.repository = repository
        self.token_manager = token_manager

    def authenticate(self, user_id: int, password: str):
        user = self.repository.get_user_by_id(user_id)
        if user and user.check_password(password):
            expiration_date = datetime.today() - timedelta(days=1)
            return self.token_manager.generate_token(user_id, expiration_date)
        return None

    def verify_token(self, token_dict: dict) -> Optional[Claim]:
        token = Token.from_dict(**token_dict)
        claim = self.token_manager.validate_token(token)

        if claim:
            return claim
        return None
