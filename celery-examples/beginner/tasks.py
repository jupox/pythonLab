# Celery task example for beginners

from celery import Celery

# Initialize a Celery instance with a broker URL
app = Celery('tasks', broker='redis://localhost:6379/0')

# Define a simple task that adds two numbers
@app.task
def add(x, y):
    """Add two numbers and return the result."""
    return x + y

# Define a task that simulates a long-running process
@app.task
def long_running_task(seconds):
    """Simulate a long-running task by sleeping for a given number of seconds."""
    import time
    time.sleep(seconds)
    return f"Task completed after {seconds} seconds."