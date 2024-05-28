################################################################################
# Filename: test_db_integrity.py
# Purpose:  File to test whether the users and midis tables in the database 
#           enforce integrity and key constraints.
# Author:   Roshni Venkat
#
# Description:
# This file contains the tests for checking whether the users and midis tables 
# throw an error when required attributes are missing. Additionally, it checks
# whether the primary and foreign key constrains are enforced in both the tables.
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
from datetime import datetime
from sqlalchemy.exc import IntegrityError

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


def test_add_incomplete_user(app):
    """
    Function to test that adding a user with incomplete data (missing name or email) 
    throws an error.

    Args:
        app (Flask): The Flask application instance.
    
    Returns:
        None
    """
    with app.app_context():
        user_without_email = User(name="IncompleteUser1")
        db.session.add(user_without_email)
        with pytest.raises(IntegrityError) as exc_info:
            db.session.commit()
        
        assert "NOT NULL constraint failed: users.email" in str(exc_info.value), \
            "IntegrityError was not raised for missing email"
        db.session.rollback()

        user_without_name = User(email="user1@gmail.com")
        db.session.add(user_without_name)
        with pytest.raises(IntegrityError) as exc_info:
            db.session.commit()
        
        assert "NOT NULL constraint failed: users.name" in str(exc_info.value), \
            "IntegrityError was not raised for missing name"
        db.session.rollback()


def test_add_incomplete_midi(app):
    """
    Function to test that MIDI fields such as title, user_id, and midi_data must not be null
    when adding an entry to the database.

    Args:
        app (Flask): The Flask application instance.
    
    Returns:
        None
    """
    with app.app_context():
        user = User(name="Test User", email="test@example.com")
        db.session.add(user)
        db.session.commit()

        # check that an error is thrown when there is no midi_data
        incomplete_midi1 = MIDI(user_id=user.user_id, title="title", date=datetime.now())
        db.session.add(incomplete_midi1)
        with pytest.raises(IntegrityError) as exc_info:
            db.session.commit()
        assert 'NOT NULL constraint failed' in str(exc_info.value), "Nullable constraint error not raised for midi_data"
        db.session.rollback()

        # check that an error is thrown when there is no title
        incomplete_midi3 = MIDI(user_id=user.user_id, date=datetime.now(), midi_data=b"midi_data")
        db.session.add(incomplete_midi3)
        with pytest.raises(IntegrityError) as exc_info:
            db.session.commit()
        assert 'NOT NULL constraint failed' in str(exc_info.value), "Nullable constraint error not raised for title"
        db.session.rollback()

        # check that an error is thrown when there is no user_id
        incomplete_midi4 = MIDI(title="title", date=datetime.now(), midi_data=b"midi_data")
        db.session.add(incomplete_midi4)
        with pytest.raises(IntegrityError) as exc_info:
            db.session.commit()
        assert 'NOT NULL constraint failed' in str(exc_info.value), "Nullable constraint error not raised for user_id"
        db.session.rollback()


def test_users_primary_key(app):
    """
    Function to test that the primary key for the Users table is automatically and uniquely assigned.

    Args:
        app (Flask): The Flask application instance.
    
    Returns:
        None
    """

    with app.app_context():
        user1 = User(name="Alice", email="alice@example.com")
        user2 = User(name="Bob", email="bob@example.com")
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        assert user1.user_id is not None
        assert user2.user_id is not None
        assert user1.user_id != user2.user_id, "Primary keys for User 1 and User 2 are not unique"


def test_midis_primary_key(app):
    """
    Function to test that the primary key for the MIDIs table is automatically and uniquely assigned.

    Args:
        app (Flask): The Flask application instance.
    
    Returns:
        None
    """
    with app.app_context():
        user = User(name="Roshni", email="roshni@example.com")
        db.session.add(user)
        db.session.commit()

        midi1 = MIDI(user_id=user.user_id, title="MIDI one", date=datetime.now(), midi_data=b"Data1")
        midi2 = MIDI(user_id=user.user_id, title="MIDI two", date=datetime.now(), midi_data=b"Data2")
        db.session.add(midi1)
        db.session.add(midi2)
        db.session.commit()

        assert midi1.midi_id is not None
        assert midi2.midi_id is not None
        assert midi1.midi_id != midi2.midi_id, "Primary keys for MIDI 1 and MIDI 2 are not unique"