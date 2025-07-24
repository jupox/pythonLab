from app.celery_app import celery_app
# from app.models import Prompt, Result # If needed for type hinting or ORM-like use
import requests
import openai
from dotenv import load_dotenv
load_dotenv()
import os
import json
from datetime import datetime
# Use the new OpenAI client for v1.x
from openai import OpenAI
from datetime import timedelta, timezone # Added timezone and timedelta
import time
import random
import string

OPENAI_API_KEY_FROM_ENV = os.getenv("OPENAI_API_KEY") 
if OPENAI_API_KEY_FROM_ENV:
    client = OpenAI(api_key=OPENAI_API_KEY_FROM_ENV)
else:
    print("Warning: OPENAI_API_KEY not found. AI features will be limited.")

@celery_app.task
def simple_task():
    """A simple Celery task that simulates work."""
    time.sleep(5)

    return "done"

@celery_app.task
def create_random_instructions_file(totalRows: int):
    """Creates a data.txt file with random instructions of a specified number of lines."""

    instructions = []

    for _ in range(totalRows):
        instruction = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        instructions.append(instruction)

    with open("data.txt", "w") as file:
        file.write("\n".join(instructions))

    return f"data.txt created with {totalRows} random instructions."

@celery_app.task
def purge_data():
    """Purges the data.txt file."""
    try:
        celery_app.control.purge()  # Clear all tasks in the queue
        celery_app.control.discard_all()  # Clear all tasks in the queue
        if not os.path.exists("data.txt"):
            return "Redis has been purged."
        # Remove the file
        os.remove("data.txt")
        return "Redis and data.txt has been purged."
    except FileNotFoundError:
        return "Redis and data.txt not purged."
    except Exception as e:
        return f"An error occurred while purge data.txt: {str(e)}"