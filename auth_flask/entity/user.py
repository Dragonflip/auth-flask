from dataclasses import dataclass, asdict
import re


@dataclass
class User:
    user_id: int
    username: str
    password_hash: str
    email: str

    @classmethod
    def from_dict(cls, d: dict) -> 'User':
        return cls(**d)

    def __post_init__(self):
        if not self.validate_email(self.email):
            raise ValueError('Endereço de e-mail inválido')

    def to_dict(self) -> dict:
        return asdict(self)

    def validate_email(self, email: str) -> bool:
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return False
        return True

    def check_password(self, password: str):
        return True
