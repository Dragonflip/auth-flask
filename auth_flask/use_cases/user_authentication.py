from datetime import timedelta, datetime
from typing import Optional
from auth_flask.entity.token import Token
from auth_flask.adapters.interfaces.token_manager import TokenManager
from auth_flask.adapters.interfaces.user_repository import UserRepo
from auth_flask.adapters.interfaces.hash import HashManager


class Authentication:
    def __init__(
        self,
        repository: UserRepo,
        token_manager: TokenManager,
        hash_manager: HashManager,
    ):
        self.repository = repository
        self.token_manager = token_manager
        self.hash_manager = hash_manager

    def authenticate(self, username: str, password: str):
        user = self.repository.get_user_by_username(username)
        if user and self.hash_manager.check_password(password, user.password):
            expiration_date = datetime.today() + timedelta(days=1)
            return self.token_manager.generate_token(
                user.username, expiration_date
            )
        return None

    def decode_token(self, token: str) -> Optional[dict]:
        claim = self.token_manager.decode_token(token)
        if claim:
            return claim
        return None
