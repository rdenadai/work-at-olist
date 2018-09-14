import os
from flask import Flask
from .controllers.principal import principal
from .controllers.api import api
from .settings import DevelopmentConfig, ProductionConfig


# Start the flask app
application = Flask(__name__)

# Import configuration depending on the environment
if os.environ.get('PYTHONHOME', None):
    application.config.from_object(ProductionConfig)
else:
    application.config.from_object(DevelopmentConfig)

# Register the apps blueprint endpoints
application.register_blueprint(principal)
application.register_blueprint(api)
