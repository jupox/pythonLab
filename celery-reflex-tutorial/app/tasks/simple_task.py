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

OPENAI_API_KEY_FROM_ENV = os.getenv("OPENAI_API_KEY") 
if OPENAI_API_KEY_FROM_ENV:
    client = OpenAI(api_key=OPENAI_API_KEY_FROM_ENV)
else:
    print("Warning: OPENAI_API_KEY not found. AI features will be limited.")

@celery_app.task
def simple_task():
    """A simple Celery task that simulates work."""
    time.sleep(15)

    return "done"