from dataclasses import dataclass
from typing import Optional
import re


@dataclass
class User:
    username: str
    password: str
    email: str
    user_id: Optional[int] = None

    @classmethod
    def from_dict(cls, d: dict) -> 'User':
        data = {
            'username': d['username'],
            'password': d['password'],
            'email': d['email'],
            'user_id': d.get('user_id'),
        }
        return cls(**data)

    def __post_init__(self):
        if not self.validate_email(self.email):
            raise ValueError('Endereço de e-mail inválido')

    def to_dict(self) -> dict:
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }

    def validate_email(self, email: str) -> bool:
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return False
        return True

    def check_password(self, password: str):
        return True
