################################################################################
# Filename: midi_controller.py
# Purpose:  Handles RESTful API routes for MIDI operations
# Author:   Benjamin Goh & Darren Seubert
#
# Description:
# This module is responsible for defining and handling all RESTful API routes
# related to MIDI operations in the application. It includes functions for
# creating, reading, updating, and deleting MIDI data.
#
# Usage (Optional):
# This module is not intended to be run as a standalone script. Instead, it should
# be imported and used in conjunction with a Flask application. For example:
#
#     from midi_controller import create_midi, get_midi
#     app.route('/midi', methods=['POST'])(create_midi)
#     app.route('/midi/<midi_id>', methods=['GET'])(get_midi)
#
# Notes:
# Ensure that the required dependencies, such as Flask and any database
# libraries, are installed and properly configured in your environment.
################################################################################

from app.database import db
from app.models.midi_model import MIDI
from app.models.user_model import User
from app.utils.status_codes import OK, CREATED, NO_CONTENT, NOT_FOUND
from app.utils.base64_converter import BinaryConverter
from app.utils.isodate_converter import DateConverter
from flask import jsonify, request
from app.utils.conversion import convert_to_midi
from app.utils.midi_to_musicxml import midi_to_musicxml
from werkzeug.utils import secure_filename
import os


def get_all_midis():
    """
    Retrieve a list of all MIDI files.

    Returns:
        tuple: A JSON list of MIDI files and the HTTP status code OK (200).
    """
    midis = MIDI.query.all()
    midis_list = []
    for midi in midis:
        # Parse date
        midi_date = midi.date.isoformat()

        # Retrieve user
        user = db.session.get(User, midi.user_id)

        # Create midi json
        midis_list.append(
            {
                "midi_id": midi.midi_id,
                "name": user.name,
                "email": user.email,
                "title": midi.title,
                "date": midi_date,
            }
        )

    return jsonify(midis_list), OK


def get_midi(midi_id):
    """
    Retrieve a single MIDI file by its ID.

    Args:
        midi_id (int): The ID of the MIDI file to retrieve.

    Returns:
        tuple: A JSON representation of the MIDI file and the HTTP status code OK (200).
    """
    midi = db.session.get(MIDI, midi_id)

    # Parse date
    midi_date = midi.date.isoformat()

    # Retrieve user
    user = db.session.get(User, midi.user_id)

    # Parse binary data
    midi_encode = BinaryConverter.encode_binary(midi.midi_data)

    # Save file
    # Decode Base64 encoded data
    midi_binary = BinaryConverter.decode_binary(midi_encode)

    # Save the decoded MIDI data to a file
    midi_file_path = f"./app/utils/midi_output/{midi.title}.mid"  # Construct a file name with MIDI ID
    with open(midi_file_path, "wb") as midi_file:
        midi_file.write(midi_binary)

    # Convert midi to music xml
    xml_output_path = midi_to_musicxml(midi_file_path)
    with open(xml_output_path, "rb") as binary_file:
        xml_output_file = binary_file.read()
    xml_data_encoded = BinaryConverter.encode_binary(xml_output_file)

    if midi:
        midi_data = {
            "midi_id": midi.midi_id,
            "name": user.name,
            "email": user.email,
            "title": midi.title,
            "date": midi_date,
            "midi_data": midi_encode,  # Return the base64-encoded MIDI data
            "xml_data": xml_data_encoded,  # Return the base64-encoded MIDI data
        }
        return jsonify(midi_data), OK
    else:
        return jsonify({"message": "MIDI not found"}), NOT_FOUND


def create_midi():
    """
    Create a new MIDI entry in the database.

    Returns:
        tuple: A JSON representation of the newly created MIDI entry and the HTTP status code CREATED (201).
    """
    name = request.form["name"]
    email = request.form["email"]
    title = request.form["title"]
    audio_file = request.files["file"]

    # Process file
    # Define file path for saving the audio file
    safe_filename = secure_filename(audio_file.filename)
    audio_file_path = os.path.join("./app/utils/audio_sample", safe_filename)
    # Ensure the directory exists
    os.makedirs(os.path.dirname(audio_file_path), exist_ok=True)

    # Save the file
    audio_file.save(audio_file_path)

    output_filename = convert_to_midi(audio_file_path)

    with open(output_filename, "rb") as binary_file:
        output_file = binary_file.read()

    midi_data_encoded = BinaryConverter.encode_binary(output_file)

    # Remove the file
    os.remove(audio_file_path)

    # Convert midi to music xml
    xml_output_path = midi_to_musicxml(output_filename)
    with open(xml_output_path, "rb") as binary_file:
        xml_output_file = binary_file.read()
    xml_data_encoded = BinaryConverter.encode_binary(xml_output_file)

    # Create User
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    # Create MIDI
    user_id = new_user.user_id
    date = DateConverter.current_time()

    new_midi = MIDI(user_id=user_id, title=title, midi_data=output_file, date=date)

    db.session.add(new_midi)
    db.session.commit()

    return (
        jsonify(
            {
                "midi_id": new_midi.midi_id,
                "name": new_user.name,
                "email": new_user.email,
                "title": new_midi.title,
                "date": new_midi.date.isoformat(),
                "midi_data": midi_data_encoded,  # Return the base64-encoded MIDI data
                "xml_data": xml_data_encoded,  # Return the base64-encoded MIDI data
            }
        ),
        CREATED,
    )


def update_midi(midi_id):
    """
    Update an existing MIDI file.

    Args:
        midi_id (int): The ID of the MIDI file to update.

    Returns:
        tuple: A JSON representation of the updated MIDI file and the HTTP status code OK (200).
    """
    updated_midi = {"id": midi_id, "name": "UpdatedMidi"}
    return jsonify(updated_midi), OK


def delete_midi(midi_id):
    """
    Delete a MIDI file.

    Args:
        midi_id (int): The ID of the MIDI file to delete.

    Returns:
        tuple: A JSON message confirming deletion and the HTTP status code NO CONTENT (204).
    """
    return jsonify({"message": f"MIDI file {midi_id} deleted successfully"}), NO_CONTENT
