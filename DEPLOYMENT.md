# Deployment

This guide outlines the process to deploy the project in a production environment using Docker.

## Log into CSL VM

Access the specific directory:

```bash
cd /nobackup
```

## Clone the Repository

Clone the project repository:

```bash
git clone https://git.doit.wisc.edu/cdis/cs/courses/cs506/sp2024/team/mondaywednesdaylecture/T_05/MelodyMapper.git

cd MelodyMapper
```

## Build and Run Containers

Use Docker Compose to build and run the containers:

```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

This command builds the images for your services and starts them in detached mode.

## Verifying Deployment

Verify the deployment:

- Ensure you are connected to the UW-Madison VPN to access internal resources.

- Access the project via http://cs506-team-05.cs.wisc.edu/.

## Updating the Deployment

To update the deployment with the latest changes from the repository:

1. Pull the latest changes:

   ```bash
   git pull origin main
   ```

2. Rebuild and restart the containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```

This will ensure any updates made to the Docker configuration or application are applied.

## Notes

- Always check that the docker-compose.prod.yml file is configured correctly for production settings, such as environment variables and exposed ports.
