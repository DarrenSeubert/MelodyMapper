################################################################################
# Filename: __init__.py
# Purpose:  [Brief description of the purpose or functionality of the file]
# Author:   Benjamin Goh
#
# Description:
# [Detailed description of the contents and functionality of the file.]
#
# Usage (Optional):
# [Instructions or examples demonstrating how to use the code in this file.
# Include any dependencies or prerequisites required for proper usage.]
#
# Notes:
# [Any additional notes, considerations, or important information
# about the file that may be relevant to developers or users.]
#
###############################################################################

import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.routes.midi_routes import midi_bp
from app.routes.user_routes import user_bp
from app.database import db


def create_app(config_object=None):
    """
    Create and configure a new Flask application instance.

    Args:
        config_object: Optional configuration object to use for the app.

    Returns:
        Flask: A new Flask application instance.
    """
    app = Flask(__name__)
    load_dotenv()

    # Configure SQLAlchemy
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = str(os.environ.get("DATABASE_URL"))
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        methods=["GET", "POST", "PUT", "DELETE"],
    )

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(midi_bp)
    app.register_blueprint(user_bp)

    return app
