from celery import Celery
import time

# Initialize Celery
celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Define a simple Celery task
@celery.task
def add(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y