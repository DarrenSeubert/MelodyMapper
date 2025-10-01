################################################################################
# Filename: Dockerfile
# Purpose:  Build and run the mysql database for the application
# Author:   Benjamin Goh & Darren Seubert
#
# Description:
# This Dockerfile sets up a MySQL database for the MelodyMapper application.
# It initializes the database using init.sql and sets environment variables
# for root password and default database creation.
#
# Usage:
# To build the Docker image, run the following command in the directory
# containing this Dockerfile:
#   docker build -t <image-name> .
#
# Notes:
# Ensure 'init.sql' is present in the same directory.
# 'init.sql' contains database initialization statements.
# MySQL root password and default database are set via environment variables.
#
###############################################################################

# Use an official MySQL runtime as a parent image
FROM mysql:latest

# Copy the database initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/