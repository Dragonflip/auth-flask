from auth_flask.frameworks.database.config.base import Base
from sqlalchemy import Column, String, Integer


class UserModel(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, username: str, email: str, password: bytes):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User(user_id={self.user_id}, username={self.username})>'
