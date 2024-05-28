################################################################################
# Filename: status_codes.py
# Purpose:  Define commonly used HTTP status codes for the Flask application.
# Author:   Benjamin Goh
#
# Description:
# This file contains constants for standard HTTP status codes used in RESTful
# responses. These constants help improve code readability and maintainability
# by providing meaningful names for numerical status codes.
#
# Usage (Optional):
# Import the status codes in your Flask view functions or controllers to use
# them in HTTP responses. For example:
#   from status_codes import OK, NOT_FOUND
#   return jsonify({'message': 'Resource found'}), OK
#   return jsonify({'error': 'Resource not found'}), NOT_FOUND
#
# Notes:
# Consider extending this file with additional status codes as needed for your
# application. Ensure that the status codes used are appropriate for the
# response context according to HTTP standards.
# References: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#
###############################################################################


# Success
OK = 200
CREATED = 201
ACCEPTED = 202
NO_CONTENT = 204

# Client Error
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
CONFLICT = 409

# Server Error
INTERNAL_SERVER_ERROR = 500
NOT_IMPLEMENTED = 501
SERVICE_UNAVAILABLE = 503
