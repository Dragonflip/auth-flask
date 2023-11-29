from auth_flask.frameworks.database.config.connection import (
    DBConnectionHandler,
)
from auth_flask.frameworks.database.config.base import Base


def initialize_database():
    # Crie as tabelas
    # Importe todos os modelos que você deseja criar no banco de dados
    from auth_flask.frameworks.database.models.user_model import UserModel

    engine = DBConnectionHandler().get_engine()
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    initialize_database()
