################################################################################
# Filename: Dockerfile
# Purpose:  Set up an Nginx server for serving a web application
# Author:   Benjamin Goh
#
# Description:
# This Dockerfile is used to create a Docker container that runs an Nginx server.
# It is specifically configured to copy a custom Nginx configuration file into the
# container, which configures Nginx to serve as a reverse proxy or static file server
# for a web application. This setup is commonly used to manage traffic to and from
# the application, handling aspects like load balancing, SSL termination, or caching.
#
# Usage:
# To build the Docker image using this Dockerfile, run the following command from
# the directory containing this Dockerfile:
#   docker build -t my-nginx .
#
# To run the Docker container from the built image, use:
#   docker run --name my-running-nginx -p 80:80 -d my-nginx
#
# This command will start an Nginx server listening on port 80 of your host machine.
#
# Notes:
# - This Dockerfile uses the latest version of the official Nginx Docker image as a
#   base. It is recommended to pin this to a specific version for production use
#   to ensure consistency and avoid unexpected changes when new versions are released.
# - The custom nginx.conf file should be thoroughly tested to ensure it meets your
#   application’s requirements and adheres to security best practices.
# - Keep in mind that any modifications to the nginx.conf file after the image is built
#   will require rebuilding the image unless volumes are used to mount configuration
#   files dynamically.
#
###############################################################################
FROM nginx:latest

# Copy the custom Nginx configuration file into the container.
COPY nginx.conf /etc/nginx/nginx.conf
