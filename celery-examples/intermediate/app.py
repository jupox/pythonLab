from flask import Flask, request, jsonify
from celery import Celery

# Initialize the Flask application
app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # URL for the message broker
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'  # URL for the result backend

# Initialize Celery with the Flask app context
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Define a simple route to trigger a Celery task
@app.route('/add', methods=['POST'])
def add_numbers():
    # Get the numbers from the request
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    # Call the Celery task
    task = add.delay(num1, num2)
    
    # Return the task ID to the client
    return jsonify({'task_id': task.id}), 202

# Define a Celery task
@celery.task
def add(x, y):
    # Simulate a long-running task
    import time
    time.sleep(5)  # Simulate delay
    return x + y

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask app in debug mode