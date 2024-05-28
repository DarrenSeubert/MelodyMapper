################################################################################
# Filename: test_connection.py
# Purpose:  Test the database connection for both User and MIDI tables.
# Author:   Darren Seubert
#
# Description:
# This file contains pytest test cases for testing the database connection
# for both User and MIDI tables.
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
from app.database import db
from app.test_config import TestingConfig
from app.models.user_model import User
from app.models.midi_model import MIDI
from datetime import datetime


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()

        # Pre-populate the database with test data for both tables
        user1 = User(name="User1", email="user1@example.com")
        user2 = User(name="User2", email="user2@example.com")
        db.session.add(user1)
        db.session.add(user2)

        midi1 = MIDI(
            user_id=1, title="MIDI 1", date=datetime.now(), midi_data=b"midi1_data"
        )
        midi2 = MIDI(
            user_id=2, title="MIDI 2", date=datetime.now(), midi_data=b"midi2_data"
        )
        db.session.add(midi1)
        db.session.add(midi2)

        db.session.commit()

        yield app
        db.session.remove()
        db.drop_all()


def test_user_table_connection(app):
    """
    Test database connection for the User table.

    Args:
        app (Flask): The Flask application instance.
    """
    with app.app_context():
        # Attempt to execute a query on the User table to test the database connection
        try:
            db.session.query(User).first()
            assert True  # Database connection successful for User table
        except Exception as e:
            assert False, f"User table connection test failed: {str(e)}"


def test_midi_table_connection(app):
    """
    Test database connection for the MIDI table.

    Args:
        app (Flask): The Flask application instance.
    """
    with app.app_context():
        # Attempt to execute a query on the MIDI table to test the database connection
        try:
            db.session.query(MIDI).first()
            assert True  # Database connection successful for MIDI table
        except Exception as e:
            assert False, f"MIDI table connection test failed: {str(e)}"
