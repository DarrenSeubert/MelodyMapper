################################################################################
# Filename: recording_model.py
# Purpose:  model for a recording
# Author:   Roshni Venkat
#
# Description:
# This file contains the model for the 'Recordings' table in the MelodyMapper database.
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
import MIDI_model as midi

class Recording:
    def __init__(self, recording_id, name, userId):
        """
        Function to initialize the recording object

        Args:
            name (String): the recording name
            user_id(int): the user id

        Returns:
            None
        """
        self.name = self.setName(name)
        self.user_id = self.setUserId(userId)
    
    def setName(self, name):
        """
        Function to set the recording name

        Args:
            name (String): the recording name

        Returns:
            None
        """
        if re.match("^[A-Za-z\s]+$", name):
            self.name = name
    
        if re.match("^[A-Za-z\s]+$", name):
            self.name = name
    
    def getName(self):
        """
        Function to get the recording name

        Args:
            name (String): the recording name

        Returns:
            The name of the recording
        """
        return self.name
    
    def setUserID(self, userId):
        """
        Function to set the user id

        Args:
            user_id (int): the user id

        Returns:
            None
        """
        if re.match("^[A-Za-z\s]+$", userId):
            self.userId = userId
    
      
    def getUserId(self):
        """
        Function to get the user id

        Args:
            user_id (int): the user id

        Returns:
            The id of the user
        """
        return self.userId
    
   