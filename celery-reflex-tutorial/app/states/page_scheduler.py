import reflex as rx
from app.utils import get_supabase_client
from datetime import datetime

class PageSchedulerState(rx.State):
    scheduled_codes: list[dict] = []
    scheduler_error_message: str = ""
    scheduler_is_loading: bool = False


    @rx.event
    async def load_scheduled_jobs(self):
        """Load all scheduled jobs from the database."""
        self.scheduled_codes = []
        self.scheduler_error_message = ""
        self.scheduler_is_loading = True

        yield rx.toast("Loading scheduled codes...")
        try:
            supabase = get_supabase_client()
            response = supabase.table("codes").select("*").order("created_at", desc=True).execute()
            if response.data:
                self.scheduled_codes = response.data
            else:
                if not response:
                    self.scheduler_error_message = f"Failed to load scheduled codes: {response.error.message}"
                else:
                    self.scheduler_error_message = "No scheduled codes found or failed to load."
        except Exception as e:
            self.scheduler_error_message = f"An error occurred while loading codes: {str(e)}"
        finally:
            self.scheduler_is_loading = False