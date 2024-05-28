################################################################################
# Filename: midi_model.py
# Purpose:  model for a MIDI
# Author:   Roshni Venkat
#
# Description:
# This file contains the model for the 'MIDIs' table in the MelodyMapper database.
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


import re

class MIDI:
    def __init__(self, recording_id, midi_data):
        """
        Function to initialize the MIDI object

        Args:
            recording_id (int): the recording id
            midi_data(bytearray): the midi data

        Returns:
            None
        """
        self.recording_id = self.setRecording(recording_id)
        self.midi_data = self.setMidiData(midi_data)

    def setRecording(self, recording_id):
        """
        Function to set the recording id

        Args:
            recording_id (int): the recording id

        Returns:
            None
        """
        if re.match("^[\d]+$", recording_id):
            self.recording_id = recording_id
    
    def getRecording(self):
        """
        Function to get the recording id

        Args:
            recording_id (int): the recording id

        Returns:
            The id of the recording
        """
        return self.recording_id
    
    def setMidiData(self, midi_data):
        """
        Function to set the midi data

        Args:
            midi_data (bytearray): the midi data

        Returns:
            None
        """
        self.midi_data = midi_data

    def getMidiData(self):
        """
        Function to get the midi data

        Args:
            midi_data (bytearray): the midi data

        Returns:
            The midi data
        """
        return self.midi_data
