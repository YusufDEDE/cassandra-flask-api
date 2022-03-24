from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    CORS(app)  # add CORS

    with app.app_context():
        from . import routes  # Import routes
        return app
