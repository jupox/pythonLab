# advanced/tasks.py

from celery import Celery
import requests

# Initialize the Celery application
app = Celery('tasks', broker='redis://localhost:6379/0')

# Example of a task that interacts with an external API
@app.task
def fetch_data_from_api(api_url):
    """
    Fetch data from an external API.
    
    :param api_url: The URL of the API to fetch data from.
    :return: The JSON response from the API.
    """
    response = requests.get(api_url)
    return response.json()

# Example of a task that processes data and interacts with a database
@app.task
def process_data(data):
    """
    Process the given data and simulate saving it to a database.
    
    :param data: The data to be processed.
    :return: A confirmation message.
    """
    # Simulate data processing
    processed_data = data.upper()  # Example processing
    # Simulate saving to a database (this is just a placeholder)
    # db.save(processed_data)
    return f"Processed and saved data: {processed_data}"

# Example of a periodic task
@app.task
def periodic_task():
    """
    A task that runs periodically.
    
    This could be used for tasks like cleaning up old data or sending reminders.
    """
    print("Periodic task executed.")  # This would be logged or handled appropriately

# Example of a task with retries
@app.task(bind=True, max_retries=3)
def unreliable_task(self):
    """
    A task that may fail and will be retried.
    
    This simulates a task that might fail intermittently.
    """
    try:
        # Simulate a task that may fail
        raise Exception("Simulated failure")
    except Exception as exc:
        # Retry the task after 5 seconds
        raise self.retry(exc=exc, countdown=5)