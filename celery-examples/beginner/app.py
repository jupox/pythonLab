from flask import Flask, jsonify
from celery import Celery
import time

# Initialize the Flask application
app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # URL for the message broker
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'  # URL for storing task results

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Define a simple Celery task
@celery.task
def add(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y

# Define a route to trigger the Celery task
@app.route('/add/<int:x>/<int:y>', methods=['GET'])
def trigger_add_task(x, y):
    task = add.delay(x, y)  # Call the Celery task asynchronously
    return jsonify({'task_id': task.id}), 202  # Return the task ID

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask server in debug mode