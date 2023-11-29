import bcrypt
from auth_flask.adapters.interfaces.hash import HashManager


class HashBcrypt(HashManager):
    def hash_password(self, password: str) -> bytes:
        password_bytes = str.encode(password)
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    def check_password(self, password: str, hashed_password: bytes) -> bool:
        password_bytes = str.encode(password)
        if bcrypt.checkpw(password_bytes, hashed_password):
            return True
        return False
