################################################################################
# Filename: isodate_converter.py
# Purpose:  Convert dates to and from ISO 8601 string format and handle current time retrieval
# Author:   Benjamin Goh
#
# Description:
# This module provides functionality for converting date objects into ISO 8601
# formatted strings and vice versa. It also includes a method for retrieving the
# current UTC time. This is particularly useful for standardized date handling
# in applications that require time data in a consistent and interoperable format.
#
# Usage:
# The DateConverter class can be used to encode and decode date information, as well
# as retrieve the current time in UTC, formatted according to ISO 8601 standards.
#
# Notes:
# The methods provided are static, as they do not depend on the state of an instance
# of the class. They can be used directly with class reference. It is important to
# ensure that the datetime objects are timezone-aware to maintain consistency and
# avoid errors in date-time conversions.
#
################################################################################

from datetime import datetime, timezone

class DateConverter:
    @staticmethod
    def encode_date(iso_date):
        """
        Convert an ISO 8601 formatted string to a datetime object.

        Args:
            iso_date (str): ISO 8601 formatted date string.

        Returns:
            datetime: A datetime object representing the provided ISO date.
        """
        return datetime.fromisoformat(iso_date)

    @staticmethod
    def decode_date(date_obj):
        """
        Convert a datetime object to an ISO 8601 formatted string.

        Args:
            date_obj (datetime): The datetime object to format.

        Returns:
            str: An ISO 8601 formatted date string.
        """
        return date_obj.isoformat()

    @staticmethod
    def current_time():
        """
        Get the current UTC time as an datetime object

        Returns:
            datetime: A datetime object representing the current date.
        """
        return datetime.now(timezone.utc)
