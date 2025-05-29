# Celery configuration for advanced usage

# This configuration file sets up Celery with advanced settings suitable for production use.
# It includes configurations for the broker, result backend, task serialization, and task routing.

from celery import Celery

def make_celery(app):
    # Create a Celery instance with the Flask app's context
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)  # Update Celery configuration with Flask app config
    return celery

# Flask application configuration
class Config:
    # URL of the message broker (e.g., RabbitMQ, Redis)
    CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Example using Redis as the broker
    # URL of the result backend (where task results are stored)
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Example using Redis for results
    # Task serialization format
    CELERY_TASK_SERIALIZER = 'json'  # Use JSON for task serialization
    # Result serialization format
    CELERY_RESULT_SERIALIZER = 'json'  # Use JSON for result serialization
    # Timezone setting
    CELERY_TIMEZONE = 'UTC'  # Set the timezone for scheduled tasks
    # Enable task routing
    CELERY_TASK_ROUTES = {
        'myapp.tasks.*': {'queue': 'default'},  # Route tasks to the default queue
    }

# Create a Celery instance
celery = make_celery(Config)  # Pass the configuration to create the Celery instance