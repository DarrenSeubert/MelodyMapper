################################################################################
# Filename: user_controller.py
# Purpose:  Handles RESTful API routes for user operations
# Author:   Benjamin Goh
#
# Description:
# This module is responsible for defining and handling all RESTful API routes
# related to user operations in the application. It includes functions for
# creating, reading, updating, and deleting user data.
#
# Usage (Optional):
# This module is not intended to be run as a standalone script. Instead, it should
# be imported and used in conjunction with a Flask application. For example:
#
#     from user_controller import create_user, get_user
#     app.route('/users', methods=['POST'])(create_user)
#     app.route('/users/<int:user_id>', methods=['GET'])(get_user)
# Notes:
# Ensure that the required dependencies, such as Flask and any database
# libraries, are installed and properly configured in your environment.
################################################################################

from app.database import db
from app.models.user_model import User
from app.utils.status_codes import OK, CREATED, NO_CONTENT, NOT_FOUND
from flask import jsonify, request


def get_all_users():
    """
    Retrieve a list of all users.

    Returns:
        tuple: A JSON list of users and the HTTP status code OK (200).
    """
    users = User.query.all()
    users_list = [
        {"user_id": user.user_id, "name": user.name, "email": user.email}
        for user in users
    ]
    return jsonify(users_list), OK


def get_user(user_id):
    """
    Retrieve a single user by its ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        tuple: A JSON representation of the user and the HTTP status code OK (200).
    """
    user = db.session.get(User, user_id)
    if user:
        user_data = {"user_id": user.user_id, "name": user.name, "email": user.email}
        return jsonify(user_data), OK
    else:
        return jsonify({"message": "User not found"}), NOT_FOUND


def create_user():
    """
    Create a new user.

    Returns:
        tuple: A JSON representation of the newly created user and the HTTP status code CREATED (201).
    """
    data = request.get_json()
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return (
        jsonify(
            {
                "user_id": new_user.user_id,
                "name": new_user.name,
                "email": new_user.email,
            }
        ),
        CREATED,
    )


def update_user(user_id):
    """
    Update an existing user.

    Args:
        user_id (int): The ID of the user to update.

    Returns:
        tuple: A JSON representation of the updated user and the HTTP status code OK (200).
    """
    user = db.session.get(User, user_id)
    if user:
        data = request.get_json()
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        db.session.commit()
        return (
            jsonify({"user_id": user.user_id, "name": user.name, "email": user.email}),
            OK,
        )
    else:
        return jsonify({"message": "User not found"}), NOT_FOUND


def delete_user(user_id):
    """
    Delete a user.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        tuple: A JSON message confirming the deletion of the user and the HTTP status code NO CONTENT (204).
    """
    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User {user_id} deleted successfully"}), NO_CONTENT
    else:
        return jsonify({"message": "User not found"}), NOT_FOUND
