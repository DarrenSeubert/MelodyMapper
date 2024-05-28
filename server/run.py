################################################################################
# Filename: run.py
# Purpose:  Serve as the entry point for running the Flask application.
# Author:   Benjamin Goh
#
# Description:
# This file imports the Flask application instance created by the create_app
# function from the app package. It then checks if the script is executed as the
# main program and runs the Flask development server.
#
# Usage (Optional):
# To start the Flask application, execute this script from the command line:
#   python run.py
#
# Notes:
# The development server is for development purposes only.
#
###############################################################################

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
