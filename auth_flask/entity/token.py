from dataclasses import dataclass, asdict
from typing import List
from datetime import datetime


@dataclass
class Token:
    token_value: str
    created_at: datetime
    expires_at: datetime
    user_id: int

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def __post_init__(self):
        if not isinstance(self.created_at, datetime):
            raise ValueError('created_at nao e um datetime')

        if not isinstance(self.expires_at, datetime):
            raise ValueError('expires_at nao e um datetime')

    def to_dict(self):
        return asdict(self)
