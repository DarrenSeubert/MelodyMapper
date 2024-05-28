################################################################################
# Filename: user_model.py
# Purpose:  model for a user
# Author:   Roshni Venkat
#
# Description:
# This file contains the model for the 'Users' table in the MelodyMapper database.
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


class User:
    def __init__(self, name, email):
        """
        Function to initialize the user object

        Args:
            user_name (String): the user name
            user_email (String): the user email

        Returns:
            None
        """
        self.name = self.setName(name)
        self.email = self.setEmail(email)
    
    def setName(self, name):
        """
        Function to set the user name

        Args:
            user_name (String): the user name

        Returns:
            None
        """
        if re.match("^[A-Za-z\s]+$", name):
            self.name = name
    
    def getName(self):
        """
        Function to get the user name

        Args:
            user_name (String): the user name

        Returns:
            The name of the user
        """
        return self.name
    
    def setEmail(self, email):
        """
        Function to set the email

        Args:
            email(String): the user email

        Returns:
            None
        """
        if re.match("^[\w_.+-]+@[\w]+\.[\w-.]+$"):
            self.email = email
    
    def getEmail(self):
        """
        Function to get the email

        Args:
            email (String): the user email

        Returns:
            The email of the user
        """
        return self.email
