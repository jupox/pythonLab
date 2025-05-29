from celery import Celery
import time

# Initialize Celery
celery = Celery('advanced_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Define a complex Celery task
@celery.task
def complex_task(x, y):
    time.sleep(5)  # Simulate a long-running task
    result = x + y
    # Additional complex logic can be added here
    return result

@celery.task
def another_complex_task(data):
    time.sleep(3)  # Simulate another long-running task
    processed_data = [d * 2 for d in data]  # Example of processing data
    return processed_data