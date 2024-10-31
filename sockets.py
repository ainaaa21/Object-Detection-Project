from flask_socketio import emit
from app import socketio  # Ensure 'app' is initialized before this import
from detection import start_detection

def send_detection_status():
    # Loop through frames and detection status from the start_detection function
    for status in start_detection():
        # Pass the detection status to all connected clients
        socketio.emit('detection_status', {'status': status})
