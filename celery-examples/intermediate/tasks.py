# Contents of /celery-examples/celery-examples/intermediate/tasks.py

from celery import Celery
import time

# Initialize a Celery application
app = Celery('tasks', broker='redis://localhost:6379/0')

# A simple task that simulates a long-running process
@app.task
def add(x, y):
    """Adds two numbers with a delay to simulate a long-running task."""
    time.sleep(5)  # Simulate a delay
    return x + y

# A background task that processes data
@app.task
def process_data(data):
    """Processes data in the background."""
    time.sleep(10)  # Simulate a longer processing time
    processed_data = [d * 2 for d in data]  # Example processing
    return processed_data

# A periodic task that runs every 10 seconds
@app.task
def periodic_task():
    """A task that runs periodically."""
    print("This task runs every 10 seconds.")

# A task that simulates sending an email
@app.task
def send_email(email_address):
    """Simulates sending an email."""
    time.sleep(3)  # Simulate email sending delay
    return f"Email sent to {email_address}"