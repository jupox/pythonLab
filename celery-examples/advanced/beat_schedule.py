from celery import Celery
from celery.schedules import crontab

# Initialize a Celery application
app = Celery('beat_schedule', broker='redis://localhost:6379/0')

# Configure the Celery Beat schedule
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,  # Executes every 30 seconds
        'args': (16, 16)  # Arguments to the task
    },
    'multiply-every-minute': {
        'task': 'tasks.multiply',
        'schedule': crontab(minute='*'),  # Executes every minute
        'args': (4, 5)  # Arguments to the task
    },
}

# Optional: Configure the timezone for the scheduled tasks
app.conf.timezone = 'UTC'

# This file sets up periodic tasks using Celery Beat.
# The 'beat_schedule' dictionary defines tasks and their schedules.
# The 'add-every-30-seconds' task will call the 'add' function from tasks.py every 30 seconds.
# The 'multiply-every-minute' task will call the 'multiply' function from tasks.py every minute.
# Make sure to run the Celery Beat scheduler alongside the worker to execute these tasks.