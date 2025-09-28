################################################################################
# Filename: Dockerfile
# Purpose:  File to test whether the backend initialization script is working
#           as expected
# Author:   Benjamin Goh & Darren Seubert
#
# Description:
# This Dockerfile is used to build a Docker image for a Python application
# that tests the initialization of a database. It sets up the environment,
# installs dependencies, and runs the application.
#
# Usage:
# To build the Docker image, run the following command in the directory
# containing this Dockerfile:
#   docker build -t <image-name> .
#
# To run the Docker container, use:
#   docker run -p 5000:5000 <image-name>
#
# Notes:
# Ensure that the 'requirements.txt' file is present in the same directory
# as this Dockerfile and contains all the necessary Python packages.
# The application is expected to be exposed on port 5000.
#
###############################################################################

# Use an official Python runtime as a parent image
FROM python:3.11.13-slim

# Install libsndfile
RUN apt-get update && apt-get install -y libsndfile1

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "run.py"]
