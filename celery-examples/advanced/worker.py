from celery import Celery

# Create a new Celery instance
app = Celery('tasks', broker='redis://localhost:6379/0')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

if __name__ == '__main__':
    # Start the Celery worker process
    app.start()