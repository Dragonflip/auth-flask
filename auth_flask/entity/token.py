from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime


@dataclass
class Token:
    token_value: str
    expires_at: Optional[datetime] = None
    username: Optional[str] = None

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return asdict(self)
