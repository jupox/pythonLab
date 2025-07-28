import reflex as rx
from app.states.page_scheduler import PageSchedulerState

def scheduled_jobs_table() -> rx.Component:
    """UI table to display scheduled jobs."""
    return rx.box(
        rx.heading("Scheduled Jobs Management", size="5", margin_bottom="2em"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Code"),
                    rx.table.column_header_cell("Numbers"),
                    rx.table.column_header_cell("Letters"),
                    rx.table.column_header_cell("Created At"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    PageSchedulerState.scheduled_codes,
                    lambda job: rx.table.row(
                        rx.table.cell(job.get("code", "N/A")),
                        rx.table.cell(job.get("numbers", "")),
                        rx.table.cell(job.get("letters", "N/A")),
                        rx.table.cell(job.get("created_at", "N/A")),
                    ),
                )
            ),
        ),
        width="100%",
        margin_top="2em",
    )

@rx.page(route="/scheduler", title="Scheduler Codes")
def scheduler_page():
    """Scheduler page layout."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Scheduler Codes", size="9"),
            rx.hstack(
                rx.button(
                    "Home",
                    on_click=rx.redirect(
                        "/"
                    ),
                    size="2",
                ),
                rx.button("Load / Refresh Schedules", on_click=PageSchedulerState.load_scheduled_jobs, is_loading=PageSchedulerState.scheduler_is_loading, size="2"),
            ),
            scheduled_jobs_table(),
            padding="2em",
            max_width="1000px",
            margin="auto",
        ),
        max_width="1000px",
        margin="auto",
    )
