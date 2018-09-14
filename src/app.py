import os
from flask import Flask
from .controllers.principal import principal
from .controllers.api import api
from .settings import DevelopmentConfig, ProductionConfig


app = Flask(__name__)

if os.environ.get('PYTHONHOME', None):
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

app.register_blueprint(principal)
app.register_blueprint(api)