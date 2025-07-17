from datetime import timedelta
from celery import Celery
from dotenv import load_dotenv
load_dotenv()
import os

REDIS_URL_FROM_ENV = os.getenv("REDIS_", "redis://redis:6379/0")
print(f"Using Redis URL: {REDIS_URL_FROM_ENV}")

celery_app = Celery(
    "worker",
    broker=REDIS_URL_FROM_ENV,
    backend=REDIS_URL_FROM_ENV,
    include=['app.tasks']
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
