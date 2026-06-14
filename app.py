from flask import Flask
from routes.auth import user_auth_bp
from services.auth_service import AuthService

app=Flask(__name__)

app.register_blueprint(user_auth_bp) #connecting the blueprint to flask application. register_blueprint() attaches the blueprint(route organized into module) to our flask app.


@user_auth_bp.route("/register", methods=["POST"]) # /auth/register
def register(data):
    return AuthService.register(data)
# /auth
# +
# /register

