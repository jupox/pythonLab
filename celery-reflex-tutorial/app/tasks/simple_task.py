from app.celery_app import celery_app
# from app.models import Prompt, Result # If needed for type hinting or ORM-like use
from dotenv import load_dotenv
load_dotenv()
import time


@celery_app.task
def simple_demo_task():
    """A simple Celery task that simulates work."""
    time.sleep(5)

    return "done"