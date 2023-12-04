from datetime import datetime, timedelta
from auth_flask.adapters.token.token_jwt import TokenJWT


def test_generate_token():
    secret_key = 'teste_secret'
    algorithm = 'HS256'
    username = 'joao'
    exp_date = datetime.utcnow() + timedelta(days=1)

    token_manager = TokenJWT()
    token_manager.__dict__['_TokenJWT__secret_key'] = secret_key
    token_manager.__dict__['_TokenJWT__secret_key'] = algorithm
    token = token_manager.generate_token(username, exp_date)
    decoded = token_manager.decode_token(token.token_value)

    assert decoded.get('username') == username
    assert decoded.get('exp')
