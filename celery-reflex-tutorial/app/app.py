"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from app.states.status import TaskStatusState

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Tasks with Celery and Reflex!", size="9"),
            rx.button(
                "Run Demo Task",
                on_click=TaskStatusState.run_simple_demo_task,
                color_scheme="teal",
                size="3",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
