"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from app.states.task_status import TaskStatus, TaskStatusState
from app.pages.scheduler import scheduler_page

class State(rx.State):
    """The app state."""

def task_table() -> rx.Component:
    """Table to display all tasks with actions."""
    return rx.box(
        rx.heading("Task Table", size="5", margin_y="2em"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Job ID"),
                    rx.table.column_header_cell("Message"),
                    rx.table.column_header_cell("Type"),
                    rx.table.column_header_cell("Status"),
                    rx.table.column_header_cell("Created At"),
                    rx.table.column_header_cell("Updated At"),
                    rx.table.column_header_cell("Actions"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    TaskStatusState.task_statuses,
                    lambda task: rx.table.row(
                        rx.table.cell(task.id),
                        rx.table.cell(task.message),
                        rx.table.cell(task.type_task),
                        rx.table.cell(task.status),
                        rx.table.cell(task.created_at),
                        rx.table.cell(task.updated_at),
                        rx.table.cell(
                            rx.hstack(
                                rx.cond((task.type_task != "purge") & ((task.status == TaskStatus.REVOKED) | (task.status == TaskStatus.SUCCESS)), 
                                    rx.button(
                                        rx.icon("play", size=18),
                                        size="1",
                                        on_click=TaskStatusState.run_again_task(task.id),
                                    ),
                                    rx.fragment(),
                                ),
                                rx.cond((task.type_task != "purge") & ((task.status == TaskStatus.RUNNING) | (task.status == TaskStatus.PENDING) | (task.status == TaskStatus)), 
                                    rx.button(
                                        rx.icon("square", size=18),
                                        size="1",
                                        on_click=TaskStatusState.stop_task(task.id),
                                    ),
                                    rx.fragment(),
                                ),
                                rx.cond(task.status != TaskStatus.SUCCESS & ( task.status != TaskStatus.ARCHIVED),
                                    rx.button(
                                        rx.icon("refresh_ccw", size=18),
                                        size="1",
                                        on_click=TaskStatusState.refresh_task_status(task.id),
                                    ),
                                    rx.fragment(),
                                ),
                                rx.cond((task.status == TaskStatus.SUCCESS) | (task.status == TaskStatus.STOPPED), 
                                    rx.button(
                                        rx.icon("archive", size=18),
                                        color_scheme="red",
                                        size="1",
                                        on_click=TaskStatusState.set_task_archived(task.id),
                                    ),
                                    rx.fragment(),
                                ),
                                spacing="2",
                            )
                        ),
                    ),
                )
            ),
        ),
        width="100%",
        margin_bottom="2em",
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Tasks with Celery and Reflex!", size="9"),
            rx.hstack(
                rx.button(
                    "Clear All Statuses",
                    on_click=TaskStatusState.run_purge_data,
                    color_scheme="red",
                    size="2",
                ),
                rx.button(
                    "Run Simple Task",
                    on_click=TaskStatusState.run_simple_task,
                    color_scheme="teal",
                    size="2",
                ),
                rx.button(
                    "Generate Instructions Task",
                    on_click=TaskStatusState.run_generate_instructions_task,
                    color_scheme="teal",
                    size="2",
                ),
                rx.button(
                    "Scheduler Codes",
                    on_click=rx.redirect(
                        "/scheduler"
                    ),
                    size="2",
                ),
            ),
            task_table(),
            padding="2em",
            max_width="1000px",
            margin="auto",
        ),
        max_width="1000px",
        margin="auto",
    )


app = rx.App()
app.add_page(index)
app.add_page(scheduler_page)