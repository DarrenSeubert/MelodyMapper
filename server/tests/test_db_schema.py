################################################################################
# Filename: test_db_schema.py
# Purpose:  file to test whether the database is created and initialized correctly
# Author:   Roshni Venkat & Darren Seubert
#
# Description:
# This file contains the tests for checking whether the database is created and
# initialized correctly.
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

import pytest
from app import create_app
from app.database import db
from app.test_config import TestingConfig
from app.models.user_model import User
from app.models.midi_model import MIDI


@pytest.fixture
def app():
    """
    Function to connect to the database.

    Args:
        None

    Returns:
        None
    """
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


def test_users_setup(app):
    """
    Function to test whether the Users table exists in the database.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    with app.app_context():
        table_exists = db.engine.dialect.has_table(db.engine.connect(), "users")
        assert table_exists


def test_midis_setup(app):
    """
    Function to test whether the MIDI table exists in the database.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    with app.app_context():
        table_exists = db.engine.dialect.has_table(db.engine.connect(), "midis")
        assert table_exists


def test_users_schema(app):
    """
    Function to test whether the Users table has the correct schema.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    with app.app_context():
        expected_columns = ["user_id", "name", "email"]
        user_columns = []
        for col in db.inspect(User.__table__).columns:
            user_columns.append(col.name)
        assert set(expected_columns) == set(user_columns)


def test_midis_schema(app):
    """
    Function to test whether the MIDI table has the correct schema.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    with app.app_context():
        expected_columns = ["midi_id", "user_id", "title", "date", "midi_data"]
        midi_columns = []
        for col in db.inspect(MIDI.__table__).columns:
            midi_columns.append(col.name)
        assert set(expected_columns) == set(midi_columns)
