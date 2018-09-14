from flask import Flask
from .controllers.principal import principal
from .controllers.api import api


app = Flask(__name__)
app.register_blueprint(principal)
app.register_blueprint(api)