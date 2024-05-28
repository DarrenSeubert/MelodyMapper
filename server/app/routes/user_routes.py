################################################################################
# Filename: user_routes.py
# Purpose:  Define routes for user-related actions in the Flask application.
# Author:   Benjamin Goh
#
# Description:
# This file creates a Blueprint for user routes and defines endpoints for
# CRUD operations on user resources, such as retrieving all users, getting a
# single user by ID, creating a new user, updating an existing user, and
# deleting a user. The routes are associated with corresponding view functions
# in the user_controller module.
#
# Usage (Optional):
# Import this Blueprint in the main application and register it to add the
# user routes to the application. For example:
#   from user_routes import user_bp
#   app.register_blueprint(user_bp)
#
# Notes:
# Ensure that the user_controller module contains the necessary view functions
# with the correct signatures to handle requests for these routes.
#
###############################################################################

from flask import Blueprint
from app.controllers import user_controller

# Create a Blueprint instance for user routes
user_bp = Blueprint("user_bp", __name__, url_prefix="/api/v1")

# Define routes for CRUD operations on user resources
user_bp.route("/users", methods=["GET"])(user_controller.get_all_users)

user_bp.route("/users/<int:user_id>", methods=["GET"])(user_controller.get_user)

user_bp.route("/users", methods=["POST"])(user_controller.create_user)

user_bp.route("/users/<int:user_id>", methods=["PUT"])(user_controller.update_user)

user_bp.route("/users/<int:user_id>", methods=["DELETE"])(user_controller.delete_user)
