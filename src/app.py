import os
from flask import Flask
from .controllers.principal import principal
from .controllers.api import api
from .settings import DevelopmentConfig, ProductionConfig


# Start the flask app
app = Flask(__name__)

# Import configuration depending on the environment
if os.environ.get('PYTHONHOME', None):
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Register the apps blueprint endpoints
app.register_blueprint(principal)
app.register_blueprint(api)