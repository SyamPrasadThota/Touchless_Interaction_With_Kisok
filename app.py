from flask import Flask, jsonify, send_from_directory
import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np
import os
import atexit  # To handle cleanup when the app stops

app = Flask(__name__)

# Load your pre-trained gesture recognition model
model = tf.keras.models.load_model('gesture_model.h5')

# Set up MediaPipe for hand gesture detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Function to release the camera when the app stops
def cleanup():
    print("Releasing the camera...")
    cap.release()
    cv2.destroyAllWindows()

# Register the cleanup function to run when the app is stopped
atexit.register(cleanup)

# Serve the HTML file at the root URL ('/')
@app.route('/')
def home():
    # Serve the index.html file from the same directory as app.py
    return send_from_directory(os.getcwd(), 'index111.html')

# Route to process the gesture
@app.route('/get_gesture', methods=['GET'])
def get_gesture():
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        return jsonify({"error": "Failed to capture frame"}), 500
    
    # Flip the frame horizontally (for better user experience)
    frame = cv2.flip(frame, 1)

    # Convert frame from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using MediaPipe to detect hand landmarks
    results = hands.process(frame_rgb)

    # If hand landmarks are detected, make predictions
    if results.multi_hand_landmarks:
        landmarks = results.multi_hand_landmarks[0]  # Get the first hand for simplicity
        input_data = []

        # Extract x, y, z for each landmark and append them
        for landmark in landmarks.landmark:
            input_data.extend([landmark.x, landmark.y, landmark.z])

        # Prepare the data for prediction (expand dimensions to match model input shape)
        input_data = np.array(input_data)
        input_data = np.expand_dims(input_data, axis=0)  # Shape: (1, 63)

        # Predict the gesture
        prediction = model.predict(input_data)

        # Get the predicted class (gesture)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # Print the predicted gesture for debugging
        print(f"Predicted Gesture: {predicted_class}")

        # Return the predicted gesture as JSON
        return jsonify({"gesture": str(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True)
