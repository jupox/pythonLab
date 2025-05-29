from flask import Flask, jsonify
from celery import Celery
from config.celery_config import celery_config
import time

# Initialize the Flask application
app = Flask(__name__)

# Configure Celery
app.config.update(celery_config)

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Define a route to trigger an advanced Celery task
@app.route('/advanced/add/<int:x>/<int:y>', methods=['GET'])
def trigger_advanced_add_task(x, y):
    task = add.delay(x, y)  # Call the Celery task asynchronously
    return jsonify({'task_id': task.id}), 202  # Return the task ID

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask server in debug mode