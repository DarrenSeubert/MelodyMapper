################################################################################
# Filename: Dockerfile
# Purpose:  Build and run the client-side React application
#           as expected
# Author:   Benjamin Goh & Darren Seubert
#
# Description:
# This Dockerfile is used to build a Docker image for a Node.js application
# that tests the initialization of a database. It sets up the environment,
# installs dependencies, and runs the application.
#
# Usage:
# To build the Docker image, run the following command in the directory
# containing this Dockerfile:
#   docker build -t <image-name> .
#
# To run the Docker container, use:
#   docker run -p 3000:3000 <image-name>
#
# Notes:
# Ensure that the 'package.json' and 'package-lock.json' (if available) are
# present in the same directory as this Dockerfile and contain all the necessary
# Node.js packages. The application is expected to be exposed on port 3000.
#
###############################################################################

# Use an official Node.js runtime as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json (if available)
COPY client/package*.json ./

# Install project dependencies
RUN npm install

# Install serve to run the production build
RUN npm install -g serve

# Bundle app source by copying all files
COPY client/. ./

# Copy env file passed by build arg
ARG ENV_FILE
COPY ${ENV_FILE} .env

# Build the app for production
RUN npm run build

# The port your app will run on
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]
