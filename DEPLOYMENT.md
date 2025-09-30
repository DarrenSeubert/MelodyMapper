# Deployment

This guide outlines the process to deploy the project in a production environment using Docker.

## Prerequisites

- Docker and Docker Compose installed on your machine or server.
- The Docker daemon is running.

## Clone the Repository

Clone the project repository:

```bash
git clone https://github.com/DarrenSeubert/MelodyMapper.git
cd MelodyMapper
```

## (Optional) Configure Environment Variables

You can override default environment variables by modifying `.env` in the project root.

## Build and Run Containers

Use Docker Compose to build and run the containers:

```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

This command builds the images for your services and starts them in detached mode.

## Verifying Deployment

- Access the application via your server’s IP or domain in a web browser (e.g., http://localhost by default).
- The frontend, backend, and database should all be running and accessible.

## Updating the Deployment

To update the production deployment with the latest changes from the repository:

1. Pull the latest changes:

   ```bash
   git pull origin main
   ```

2. Rebuild and restart the containers:

   ```bash
   docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
   ```

This will ensure any updates made to the Docker configuration or application are applied.

## Notes

- Always check that the `docker-compose.prod.yml` file is configured correctly for your production settings, such as environment variables and exposed ports.
- For custom domains or HTTPS, you must update `nginx/nginx.conf` to set your domain name and SSL certificate paths. See Nginx documentation for details. By default, the app runs on HTTP and localhost only.
