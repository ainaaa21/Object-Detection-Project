import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r"D:\Desktop\best_yolov8n.pt")

def start_detection():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
    # Start a loop to read frames from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Flip the frame horizontally (mirror image)
        frame = cv2.flip(frame, 1)
        # Perform prediction using the YOLO model
        results = model.predict(source=frame, show=False, conf=0.5)
        # Annotate the frame with detection results
        annotated_frame = results[0].plot()

        # Determine the status based on detection results
        if len(results[0].boxes) == 0:
            status = "No Detection"
        else:
            # Join the names of detected objects into a status string
            status = ", ".join([model.names[int(result.cls)] for result in results[0].boxes])

        # Encode the annotated frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Yield the frame and status to be used by the Flask application
        yield frame, status

    # Release the webcam and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
