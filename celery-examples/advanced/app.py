from flask import Flask, request, jsonify
from celery import Celery
import time

# Initialize Flask application
app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Define a Celery task
@celery.task
def long_running_task(data):
    # Simulate a long-running task
    time.sleep(10)  # Simulates a delay
    return f"Processed data: {data}"

# Define a route to trigger the Celery task
@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('data')
    task = long_running_task.apply_async(args=[data])
    return jsonify({"task_id": task.id}), 202

# Define a route to check the task status
@app.route('/status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = long_running_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result
        }
    else:
        response = {
            'state': task.state,
            'error': str(task.info),  # Exception raised in the task
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode