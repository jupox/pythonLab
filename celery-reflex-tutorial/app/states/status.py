from app.tasks.simple_task import simple_demo_task
import reflex as rx
import time

class TaskStatusState(rx.State):
    """State for managing Celery task statuses."""
    # Dictionary mapping task_id to a dict with status and optional message
    task_statuses: dict[str, dict] = {}

    @rx.event
    def set_task_status(self, task_id: str, status: str, message: str = ""):
        """Set or update the status and message for a task."""
        self.task_statuses[task_id] = {"status": status, "message": message}

    @rx.event
    def remove_task_status(self, task_id: str):
        """Remove a task status entry."""
        if task_id in self.task_statuses:
            del self.task_statuses[task_id]

    @rx.event
    def clear_all_statuses(self):
        """Clear all task statuses."""
        self.task_statuses = {}

    @rx.event
    def run_simple_demo_task(self):
        """Trigger the Celery simple_demo_task and show toasts."""
        simple_demo_task.delay()
        task_id = simple_demo_task.request.id
        self.set_task_status(task_id, "running", "Task is running...")
        yield rx.toast.success("Simple Task is running!", duration=2000)