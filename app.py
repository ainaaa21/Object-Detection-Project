from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
from detection import start_detection

# Initialize the Flask application
app = Flask(__name__)
#Initialize the SocketIO extension
socketio = SocketIO(app)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the detection page
@app.route('/detection')
def detection():
    return render_template('detection.html')

# Route for the video feed
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Function to generate frames from the detection function
def generate_frames():
    for frame, status in start_detection():
        # Pass the detection status to the client
        socketio.emit('detection_status', {'status': status})
        # Yield the frame in the required format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Run the application
if __name__ == '__main__':
    socketio.run(app, debug=True)
