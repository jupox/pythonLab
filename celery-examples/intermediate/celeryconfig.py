# Celery configuration for the intermediate examples

# Import the necessary modules from Celery
from celery import Celery

# Create a Celery instance with the name of the current module
app = Celery('celery_examples.intermediate')

# Load configuration from a separate configuration object
app.config_from_object('celeryconfig')

# Automatically discover tasks from the tasks module
app.autodiscover_tasks(['celery_examples.intermediate.tasks'])

# Define a simple configuration for the Celery broker and result backend
broker_url = 'redis://localhost:6379/0'  # Using Redis as the message broker
result_backend = 'redis://localhost:6379/0'  # Using Redis to store task results

# Task serialization format
task_serializer = 'json'  # Use JSON for serializing task messages
result_serializer = 'json'  # Use JSON for serializing task results

# Enable task time limits
task_time_limit = 300  # Set a time limit of 5 minutes for tasks

# Enable task retries
task_annotations = {
    'tasks.add': {'max_retries': 3, 'default_retry_delay': 10},  # Retry the 'add' task up to 3 times with a 10-second delay
}

# This configuration allows for a more structured and scalable Celery setup
# suitable for intermediate-level applications using Flask.