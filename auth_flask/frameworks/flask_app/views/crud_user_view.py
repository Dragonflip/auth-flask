from flask import Flask, jsonify, request, Blueprint
from auth_flask.entity.user import User
from auth_flask.adapters.database.user_repository import DatabaseAdapter
from auth_flask.frameworks.database.config.connection import (
    DBConnectionHandler,
)
from auth_flask.adapters.hash.hash_password import HashBcrypt
from auth_flask.frameworks.database.models.user_model import UserModel
from auth_flask.use_cases.user_crud import UserCrud
from auth_flask.adapters.serializers.user import UserSerializer
from auth_flask.frameworks.flask_app.views.authentication_view import (
    token_required,
)

# app = Flask(__name__)
app = Blueprint('user', __name__)

hash_manager = HashBcrypt()
db_connection_handler = DBConnectionHandler()
db_adapter = DatabaseAdapter(db_connection_handler, hash_manager)
user_crud = UserCrud(db_adapter)


@app.route('/users', methods=['GET'])
@token_required
def get_all_users():
    users = user_crud.list_users()
    user_list = [UserSerializer.serialize(user) for user in users]
    return jsonify({'users': user_list})


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = user_crud.get_user_by_id(id)
    return jsonify(UserSerializer.serialize(user))


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
    )
    user_crud.create_user(new_user)
    return jsonify({'message': 'User created successfully'}), 201


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user_crud.update_user(id, data)
    return jsonify({'message': 'User updated successfully'}), 201


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_crud.delete_user_by_id(id)
    return jsonify({'message': 'User deleted successfully'}), 201
