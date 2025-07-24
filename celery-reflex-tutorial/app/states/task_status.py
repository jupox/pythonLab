from app.tasks.simple_task import create_random_instructions_file, purge_data, simple_task
from app.models import TaskItem
import reflex as rx
from datetime import datetime
import uuid
from app.celery_app import celery_app  # Import the Celery app instance
from celery.result import AsyncResult
from enum import Enum
import random

class TaskStatus(Enum):
    RUNNING = "RUNNING"
    RUNNING_AGAIN = "RUNNING_AGAIN"
    ARCHIVED = "ARCHIVED"
    STOPPED = "STOPPED"
    SUCCESS = "SUCCESS"
    REVOKED = "REVOKED"
    PENDING = "PENDING"


class TaskStatusState(rx.State):
    """State for managing Celery task statuses."""
    # Dictionary mapping task_id to a dict with status and optional message
    task_statuses: list[TaskItem] = []

    @rx.event
    def set_task_status(self, task_id: int, status: str, message: str = "", type_task="simple"):
        """Set or update the status and message for a task."""
        newTask = TaskItem(
            id=task_id,
            status=status,
            message=message,
            type_task=type_task,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        # Check if the task already exists
        existing_task = next((t for t in self.task_statuses if t.id == task_id), None)
        if existing_task:
            # Update existing task
            existing_task.status = status
            existing_task.message = message
            existing_task.updated_at = datetime.now()
        else:
            # Add new task
            self.task_statuses.append(newTask)
        
    @rx.event
    def clear_all_statuses(self):
        """Clear all task statuses."""
        self.task_statuses = []

    @rx.event
    def run_simple_task(self):
        """Trigger the Celery simple_demo_task and show toasts."""
        result = simple_task.delay()
        aux_id = str(uuid.uuid4())         
        task_id = result.id or aux_id
        self.set_task_status(task_id, TaskStatus.RUNNING, "Simple Task")
        yield rx.toast.success("Simple Task is running!", duration=2000)

    @rx.event
    def run_again_task(self, task_id: str):
        """Run a task again by its ID."""
        for task in self.task_statuses:
            if task.id == task_id:
                if task.type_task == "simple":
                    simple_task.apply_async(task_id=task.id)
                    task.status = TaskStatus.RUNNING_AGAIN
                    task.message = "Task is running again."
                    task.updated_at = datetime.now()
                elif task.type_task == "File_Task":
                    create_random_instructions_file.apply_async(task_id=task.id)
                    task.status = TaskStatus.RUNNING_AGAIN
                    task.message = "File Task is running again."
                    task.updated_at = datetime.now()
                yield rx.toast.success(f"Task {task_id} is running again!", duration=2000)
                return
        yield rx.toast.error("Task not found!", duration=2000)
    

    @rx.event
    def set_task_archived(self, task_id: str):
        """Archive a task by its ID."""
        for task in self.task_statuses:
            if task.id == task_id:
                task.status = TaskStatus.ARCHIVED
                task.message = "Task has been archived."
                task.updated_at = datetime.now()
                yield rx.toast.info("Task archived successfully!", duration=2000)
                return
        yield rx.toast.error("Task not found!", duration=2000)

    @rx.event
    def refresh_task_status(self, task_id: str):
        """Refresh the status of a task by its ID."""
        result = AsyncResult(task_id)

        if "purge" in (str(result.result) if result.result else ""):
            for task in self.task_statuses:
                if task_id != task.id:
                    AsyncResult(task.id).forget()  # Clear other tasks
            self.task_statuses = [task for task in self.task_statuses if task.id == task_id]
            yield rx.toast.info(f"List of tasks purged!", duration=2000)
            
        for task in self.task_statuses:            
            if task.id == task_id:
                if result.status != task.status:
                    task.status = result.status
                    task.message = str(result.result) if result.result else "No result yet."
                    task.updated_at = datetime.now()                    
                    yield rx.toast.info(f"Task {task_id} status refreshed!", duration=2000)
                return
                    
        yield rx.toast.error("Task not found!", duration=2000)

    @rx.event
    def stop_task(self, task_id: str):
        """Stop a task by its ID."""
        for task in self.task_statuses:
            if task.id == task_id:
                # Attempt to revoke the task using Celery
                try:
                    celery_app.control.revoke(task_id, terminate=True)
                except Exception as e:
                    yield rx.toast.error(f"Failed to stop task {task_id}: {str(e)}", duration=2000)
                    return
                task.status = TaskStatus.STOPPED
                task.message = "Task has been stopped."
                task.updated_at = datetime.now()
                yield rx.toast.warning(f"Task {task_id} has been stopped!", duration=2000)
                return
        yield rx.toast.error("Task not found!", duration=2000)


    @rx.event
    def run_generate_instructions_task(self):
        num_lines = random.randint(1, 1000000)
        result = create_random_instructions_file.delay(num_lines)
        aux_id = str(uuid.uuid4())         
        task_id = result.id or aux_id
        self.set_task_status(task_id, TaskStatus.RUNNING, f"File_Task with {num_lines} lines", "generate")
        yield rx.toast.success("File Task is running!", duration=2000)

    @rx.event
    def run_purge_data(self):
        """Purge the data.txt file and clear the task queue."""
        result = purge_data.delay()
        aux_id = str(uuid.uuid4())         
        task_id = result.id or aux_id
        self.set_task_status(task_id, TaskStatus.RUNNING, "Purging redis and data.txt", "purge")
        yield rx.toast.success("Purging data.txt is running!", duration=2000)