
# celery-reflex-tutorial: Celery Redis Reflex - Docker - Python

**Running the Application with Docker Compose:**

1.  **Ensure No Port Conflicts**:
    The `docker-compose.yml` file maps several ports to your host machine (e.g., 8000 for Kong, 3000 for the web app, 6379 for Redis, 54322 for Supavisor/Postgres). Ensure these ports are free on your machine or adjust them in the `.env` file (for Supabase ports) or `docker-compose.yml` (for project service ports).

2.  **Build and Start Services**:
    Open your terminal in the project root directory (where `docker-compose.yml` and `.env` are located) and run:
    ```bash
    docker-compose up --build -d
    ```
    *   `--build`: Forces Docker Compose to build the images from your Dockerfile (for `web` and `worker` services) before starting the services.
    *   `-d`: Runs the services in detached mode (in the background).

    This command will:
    *   Pull official images for Supabase services and Redis if you don't have them locally.
    *   Build the Docker image for your application.
    *   Start all defined services, including the full Supabase stack and your application's `web-celery-reflex`, `worker-celery`, and `redis-celery` services.