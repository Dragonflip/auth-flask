from flask import Flask
from auth_flask.frameworks.flask_app.views.crud_user_view import (
    app as user_app,
)
from auth_flask.frameworks.flask_app.views.authentication_view import (
    app as authentication_app,
)

app = Flask(__name__)
app.register_blueprint(user_app)
app.register_blueprint(authentication_app)


if __name__ == '__main__':
    app.run(debug=True)
