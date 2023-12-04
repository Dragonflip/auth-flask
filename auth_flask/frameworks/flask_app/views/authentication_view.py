from flask import jsonify, request, Blueprint
from auth_flask.adapters.database.user_repository import DatabaseAdapter
from auth_flask.frameworks.database.config.connection import (
    DBConnectionHandler,
)
from auth_flask.adapters.hash.hash_password import HashBcrypt
from auth_flask.adapters.token.token_jwt import TokenJWT
from auth_flask.use_cases.user_authentication import Authentication
from auth_flask.entity.token import Token


app = Blueprint('authentication', __name__)

hash_manager = HashBcrypt()
db_connection_handler = DBConnectionHandler()
db_adapter = DatabaseAdapter(db_connection_handler, hash_manager)
token_manager = TokenJWT()
use_case_authentication = Authentication(
    db_adapter, token_manager, hash_manager
)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    token = use_case_authentication.authenticate(username, password)
    if token:
        return jsonify(access_token=token), 200
    return jsonify({'msg': 'Credenciais Invalidas'})


def token_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return (
                jsonify(
                    {
                        'message': 'token is missing',
                    }
                ),
                401,
            )
        try:
            data = use_case_authentication.decode_token(token)
            current_user = db_adapter.get_user_by_username(data['username'])
        except Exception as e:
            print(e)
            return jsonify({'message': 'token invalid or expired'}), 401
        return f(*args, **kwargs)

    return decorated
