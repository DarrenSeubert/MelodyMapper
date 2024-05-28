################################################################################
# Filename: base64_converter.py
# Purpose:  To encode and decode binary data to and from Base64 format
# Author:   Benjamin Goh
#
# Description:
# This module provides utilities to convert binary data into a Base64-encoded
# string and to decode a Base64-encoded string back into binary data. This is
# particularly useful for handling data that needs to be safely transmitted over
# media that are designed to deal with textual data. It helps to ensure that
# binary data remains intact without modification during transport.
#
# Usage:
# The BinaryConverter class can be used to encode binary data like images, files,
# or any binary content to a Base64 string and to decode such strings back to
# binary form.
#
# Notes:
# Base64 encoding is typically used when there is a need to encode binary data,
# especially when that data needs to be stored and transferred over media that
# are designed to deal with textual data. This encoding helps to ensure that
# the data remains intact without modification during transport.
#
###############################################################################
import base64

class BinaryConverter:
    @staticmethod
    def encode_binary(binary_data):
        """
        Encode binary data to a Base64 string.

        Args:
            binary_data (bytes): The binary data to encode.

        Returns:
            str: A Base64 encoded string.
        """
        return base64.b64encode(binary_data).decode('utf-8')

    @staticmethod
    def decode_binary(encoded_string):
        """
        Decode a Base64 string back to binary data.

        Args:
            encoded_string (str): The Base64 encoded string to decode.

        Returns:
            bytes: The original binary data.
        """
        return base64.b64decode(encoded_string)
