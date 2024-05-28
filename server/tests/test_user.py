################################################################################
# Filename: test_user.py
# Purpose:  Test the user-related API endpoints.
# Author:   Benjamin Goh
#
# Description:
# This file contains pytest test cases for testing the CRUD operations on user
# resources provided by the Flask application. It tests the endpoints for
# retrieving all users, getting a single user by ID, creating a new user,
# updating an existing user, and deleting a user.
#
# Usage (Optional):
# Run the tests using the pytest command:
#   python -m pytest
#
# Notes:
# The tests assume that the application is configured for testing and that
# the test database is properly set up.
#
###############################################################################

import pytest
from app import create_app
from app.utils.status_codes import OK, CREATED, NO_CONTENT
from app.database import db
from app.test_config import TestingConfig
from app.models.user_model import User


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()

        # Pre-populate the database with test data
        user1 = User(name="User1", email="user1@example.com")
        user2 = User(name="User2", email="user2@example.com")
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_all_users(client):
    """
    Test retrieving a list of all user.

    Args:
        client (FlaskClient): The test client for the application.
    """
    USERS_API_URL = "api/v1/users"
    response = client.get(USERS_API_URL)
    assert response.status_code == OK
    assert response.json == [
        {"user_id": 1, "name": "User1", "email": "user1@example.com"},
        {"user_id": 2, "name": "User2", "email": "user2@example.com"},
    ]


def test_get_user(client):
    """
    Test retrieving a single user by its ID.

    Args:
        client (FlaskClient): The test client for the application.
    """
    USERS_API_URL = "api/v1/users/1"
    response = client.get(USERS_API_URL)
    assert response.status_code == OK
    assert response.json == {
        "user_id": 1,
        "name": "User1",
        "email": "user1@example.com",
    }


def test_create_user(client):
    """
    Test creating a new user.

    Args:
        client (FlaskClient): The test client for the application.
    """
    USERS_API_URL = "api/v1/users"
    NEW_USER_DATA = {"name": "User3", "email": "user3@example.com"}
    response = client.post(USERS_API_URL, json=NEW_USER_DATA)
    assert response.status_code == CREATED
    assert response.json == {
        "user_id": 3,
        "name": "User3",
        "email": "user3@example.com",
    }


def test_update_user(client):
    """
    Test updating an existing user.

    Args:
        client (FlaskClient): The test client for the application.
    """
    USERS_API_URL = "api/v1/users/1"
    UPDATE_USER_DATA = {"name": "User1Modified", "email": "user1newemail@example.com"}
    response = client.put(USERS_API_URL, json=UPDATE_USER_DATA)
    assert response.status_code == OK
    assert response.json == {
        "user_id": 1,
        "name": "User1Modified",
        "email": "user1newemail@example.com",
    }


def test_delete_user(client):
    """
    Test deleting a user.

    Args:
        client (FlaskClient): The test client for the application.
    """
    USERS_API_URL = "api/v1/users/1"
    response = client.delete(USERS_API_URL)
    assert response.status_code == NO_CONTENT
