################################################################################
# Filename: test_midi.py
# Purpose:  Test the MIDI-related API endpoints.
# Author:   Benjamin Goh
#
# Description:
# This file contains pytest test cases for testing the CRUD operations on MIDI
# resources provided by the Flask application. It tests the endpoints for
# retrieving all MIDIs, getting a single MIDI by ID, creating a new MIDI,
# updating an existing MIDI, and deleting a MIDI.
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

from io import BytesIO
import pytest
from app import create_app
from app.utils.status_codes import OK, CREATED, NO_CONTENT
from app.database import db
from app.test_config import TestingConfig
from app.models.user_model import User
from app.models.midi_model import MIDI
from app.utils.base64_converter import BinaryConverter
from app.utils.isodate_converter import DateConverter

ISODATE = "2024-04-09T12:34:56"
DATE = DateConverter.encode_date(ISODATE)


# For actual file data test
# MIDI1_DATA = read_midi_file("server/tests/resources/midi1.mid")
# MIDI2_DATA = read_midi_file("server/tests/resources/midi2.mid")

# For simple data test
MIDI1_ENCODED = BinaryConverter.encode_binary(b"MidiData1")
MIDI2_ENCODED = BinaryConverter.encode_binary(b"MidiData2")
MIDI1_DATA = BinaryConverter.decode_binary(MIDI1_ENCODED)
MIDI2_DATA = BinaryConverter.decode_binary(MIDI2_ENCODED)


def read_midi_file(file_path):
    """Read a MIDI file and return its binary data."""
    with open(file_path, "rb") as file:
        return file.read()


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()

        # Pre-populate the database with test data
        user1 = User(name="User1", email="User1@gmail.com")
        user2 = User(name="User2", email="User2@gmail.com")
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        midi1 = MIDI(user_id=1, title="Midi1", date=DATE, midi_data=MIDI1_DATA)
        midi2 = MIDI(user_id=2, title="Midi2", date=DATE, midi_data=MIDI2_DATA)
        db.session.add(midi1)
        db.session.add(midi2)
        db.session.commit()

        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_all_midis(client):
    """
    Test retrieving a list of all MIDI files.

    Args:
        client (FlaskClient): The test client for the application.
    """
    MIDIS_API_URL = "api/v1/midis"
    response = client.get(MIDIS_API_URL)
    assert response.status_code == OK
    assert response.json == [
        {
            "midi_id": 1,
            "name": "User1",
            "email": "User1@gmail.com",
            "title": "Midi1",
            "date": ISODATE,
        },
        {
            "midi_id": 2,
            "name": "User2",
            "email": "User2@gmail.com",
            "title": "Midi2",
            "date": ISODATE,
        },
    ]

# REQUIRES REFACTORING OF CODE.
# def test_get_midi(client):
#     """
#     Test retrieving a single MIDI file by its ID.

#     Args:
#         client (FlaskClient): The test client for the application.
#     """
#     MIDIS_API_URL = "api/v1/midis/1"
#     response = client.get(MIDIS_API_URL)
#     assert response.status_code == OK
#     del response["xml_data"]
#     assert response.json == {
#         "midi_id": 1,
#         "name": "User1",
#         "email": "User1@gmail.com",
#         "title": "Midi1",
#         "date": ISODATE,
#         "midi_data": MIDI1_ENCODED,
#     }


# def test_create_midi(client):
#     """
#     Test creating a new MIDI file.

#     Args:
#         client (FlaskClient): The test client for the application.
#     """
#     # Setup for test
#     MIDIS_API_URL = "api/v1/midis"
#     NEW_MIDI = {
#         "name": "John",
#         "email": "john@gmail.com",
#         "title": "A Random Song",
#         "file": (BytesIO(b'my file contents'), 'file_name.mp3'),
#     }

#     # Check file
#     with open('./server/app/controllers/converted-example.midi', 'rb') as binary_file:
#         output_file = binary_file.read()
#     midi_data_encoded = BinaryConverter.encode_binary(output_file)

#     response = client.post(MIDIS_API_URL, data=NEW_MIDI, content_type='multipart/form-data')
#     assert response.status_code == CREATED

#     # Check response except date
#     response_json = response.json
#     del response_json["date"]
#     assert response_json == {
#         "midi_id": 3,
#         "name": "John",
#         "email": "john@gmail.com",
#         "title": "A Random Song",
#         "midi_data": midi_data_encoded,
#     }


def test_update_midi(client):
    """
    Test updating an existing MIDI file.

    Args:
        client (FlaskClient): The test client for the application.
    """
    MIDIS_API_URL = "api/v1/midis/1"
    response = client.put(MIDIS_API_URL)
    assert response.status_code == OK
    assert response.json == {"id": 1, "name": "UpdatedMidi"}


def test_delete_midi(client):
    """
    Test deleting a MIDI file.

    Args:
        client (FlaskClient): The test client for the application.
    """
    MIDIS_API_URL = "api/v1/midis/1"
    response = client.delete(MIDIS_API_URL)
    assert response.status_code == NO_CONTENT
