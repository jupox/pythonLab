# Celery Examples - Beginner README

# Introduction
This directory contains beginner-level examples demonstrating how to use Celery with a Flask application. Celery is an asynchronous task queue/job queue based on distributed message passing. It is used to handle background tasks and can be integrated easily with Flask.

# Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Flask
- Celery
- A message broker (e.g., Redis or RabbitMQ)

# Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd celery-examples/beginner
   ```

2. Install the required packages:
   ```
   pip install Flask Celery redis
   ```

# Running the Application
1. Start your message broker (e.g., Redis):
   ```
   redis-server
   ```

2. Start the Celery worker in a new terminal:
   ```
   celery -A tasks worker --loglevel=info
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Access the application in your web browser at `http://localhost:5000`.

# Usage
- The application has a simple route that triggers a Celery task to add two numbers.
- You can test the functionality by navigating to the root URL, which will call the Celery task and return the result.

# Conclusion
This beginner example provides a basic understanding of how to set up and use Celery with Flask. For more advanced examples, please refer to the intermediate and advanced directories.