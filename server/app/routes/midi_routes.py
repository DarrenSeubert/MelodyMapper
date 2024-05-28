################################################################################
# Filename: midi_routes.py
# Purpose:  Define routes for MIDI-related actions in the Flask application.
# Author:   Benjamin Goh
#
# Description:
# This file creates a Blueprint for MIDI routes and defines endpoints for
# CRUD operations on MIDI resources, such as retrieving all MIDIs, getting a
# single MIDI by ID, creating a new MIDI, updating an existing MIDI, and
# deleting a MIDI. The routes are associated with corresponding view functions
# in the midi_controller module.
#
# Usage (Optional):
# Import this Blueprint in the main application and register it to add the
# MIDI routes to the application. For example:
#   from midi_routes import midi_bp
#   app.register_blueprint(midi_bp)
#
# Notes:
# Ensure that the midi_controller module contains the necessary view functions
# with the correct signatures to handle requests for these routes.
#
###############################################################################

from flask import Blueprint
from app.controllers import midi_controller

# Create a Blueprint instance for MIDI routes
midi_bp = Blueprint("midi_bp", __name__, url_prefix="/api/v1")

# Define routes for CRUD operations on MIDI resources
midi_bp.route("/midis", methods=["GET"])(midi_controller.get_all_midis)

midi_bp.route("/midis/<int:midi_id>", methods=["GET"])(midi_controller.get_midi)

midi_bp.route("/midis", methods=["POST"])(midi_controller.create_midi)

midi_bp.route("/midis/<int:midi_id>", methods=["PUT"])(midi_controller.update_midi)

midi_bp.route("/midis/<int:midi_id>", methods=["DELETE"])(midi_controller.delete_midi)
