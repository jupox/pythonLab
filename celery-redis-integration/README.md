# Celery and Redis Integration Project

This project demonstrates how to integrate Celery with Redis in both beginner and advanced examples. It provides a simple Flask application that utilizes Celery for asynchronous task processing.

## Project Structure

```
celery-redis-integration
├── beginner
│   ├── app.py                # Simple Flask app with a basic Celery task
│   ├── tasks.py              # Defines the Celery task for adding two numbers
│   └── requirements.txt       # Lists dependencies for the beginner project
├── advanced
│   ├── app.py                # More complex Flask app with advanced task handling
│   ├── tasks
│   │   ├── __init__.py       # Empty initializer for the tasks package
│   │   └── advanced_task.py   # Defines more complex Celery tasks
│   ├── config
│   │   └── celery_config.py   # Configuration settings for Celery
│   └── requirements.txt       # Lists dependencies for the advanced project
└── README.md                  # Documentation for setting up and running the project
```

## Prerequisites

- Python 3.x
- Redis server running locally

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd celery-redis-integration
   ```

2. Install the required dependencies for the beginner project:
   ```
   cd beginner
   pip install -r requirements.txt
   ```

3. For the advanced project, install the dependencies:
   ```
   cd ../advanced
   pip install -r requirements.txt
   ```

## Running the Applications

### Beginner Example

1. Start the Redis server if it's not already running:
   ```
   redis-server
   ```

2. Run the Flask application:
   ```
   cd beginner
   python app.py
   ```

3. Trigger the Celery task by visiting:
   ```
   http://localhost:5000/add/<x>/<y>
   ```
   Replace `<x>` and `<y>` with the numbers you want to add.

### Advanced Example

1. Start the Redis server if it's not already running:
   ```
   redis-server
   ```

2. Run the Flask application:
   ```
   cd advanced
   python app.py
   ```

3. Access the advanced routes to trigger more complex tasks as defined in the application.

## Conclusion

This project serves as a foundational guide for integrating Celery with Redis in Python applications. The beginner example provides a straightforward introduction, while the advanced example showcases more complex task management and application structure.