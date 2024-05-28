################################################################################
# Filename: midi_to_xml.py
# Purpose:  Convert MIDI file to MusicXML for sheet music.
# Author:   Darren Seubert
#
# Description:
# This script converts a MIDI file into a MusicXML file suitable for sheet music
# using the music21 library.
#
# Usage:
# Run this script with the path to the MIDI file as an argument.
# Ensure that the music21 library is installed in your Python environment.
#
################################################################################

import os
from music21 import converter


def midi_to_musicxml(midi_file):
    """
    Convert MIDI file to MusicXML format.

    Args:
        midi_file (str): The path to the MIDI file.

    Returns:
        str: The path to the generated MusicXML file.
    """
    # Load MIDI file
    score = converter.parse(midi_file)

    # Define output directory for MusicXML files
    musicxml_output_folder = "./musicxml_output"

    # Create the output directory if it doesn't exist
    if not os.path.exists(musicxml_output_folder):
        os.makedirs(musicxml_output_folder)

    # Convert MIDI to MusicXML
    musicxml_file = os.path.join(
        musicxml_output_folder, os.path.basename(midi_file).replace(".mid", ".musicxml")
    )
    score.write("musicxml", musicxml_file)

    return musicxml_file
