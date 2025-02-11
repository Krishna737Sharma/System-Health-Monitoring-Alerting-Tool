from flask import Flask, jsonify, request
import psutil
import database
import sqlite3
app = Flask(__name__)

# Initialize the database
database.init_db()

# Route to fetch system metrics (CPU, memory, disk usage)
@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Define thresholds for alerts
    cpu_threshold = 80.0
    memory_threshold = 80.0
    disk_threshold = 90.0

    # Check if thresholds are exceeded and add alerts
    if cpu_usage > cpu_threshold:
        database.add_alert('CPU', cpu_threshold, 'Active')
    if memory_usage > memory_threshold:
        database.add_alert('Memory', memory_threshold, 'Active')
    if disk_usage > disk_threshold:
        database.add_alert('Disk', disk_threshold, 'Active')

    # Return the metrics as JSON
    return jsonify({
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage
    })

# Route to add metadata (name, environment, location)
@app.route('/api/metadata', methods=['POST'])
def add_metadata():
    data = request.json
    name = data.get('name')
    environment = data.get('environment')
    location = data.get('location')
    database.add_metadata(name, environment, location)
    return jsonify({'message': 'Metadata added successfully'}), 201

# Route to fetch alerts
@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    conn = sqlite3.connect('system_health.db')
    c = conn.cursor()
    c.execute("SELECT * FROM alerts")
    alerts = c.fetchall()
    conn.close()
    return jsonify({'alerts': alerts})

# Root route
@app.route('/')
def home():
    return "Welcome to the System Health Monitoring Tool! Use /api/metrics, /api/metadata, and /api/alerts to interact with the API."

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)