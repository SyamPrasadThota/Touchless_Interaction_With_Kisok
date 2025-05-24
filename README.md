## 📍 Project Overview

**Touchless Interaction With Kiosk** is an AI-powered flight kiosk simulation that allows users to interact with an on-screen airport kiosk using hand gestures. Built with computer vision and deep learning, this project replaces physical touch with gesture recognition — enhancing hygiene, accessibility, and user experience in public areas like airports.

It uses a trained gesture recognition model with real-time webcam input to allow users to control the interface intuitively.

---

## ✨ Features

* Touchless gesture-based interface using webcam input
* Real-time hand detection with MediaPipe
* Gesture classification using a trained deep learning model (`gesture_model.h5`)
* Airport kiosk simulation: check-in, help, maps, and flight info
* Lightweight and fast using Flask backend
* Responsive HTML/CSS frontend

---

## ✅ Prerequisites

* Python 3.8+
* pip (Python package manager)
* A webcam-enabled device
* Virtual environment (recommended)

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/Touchless_Interaction_With_Kisok.git
cd Touchless_Interaction_With_Kisok
```

2. **Create a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# OR
source venv/bin/activate   # For macOS/Linux
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧠 Technologies Used

* **Flask** – Web framework
* **OpenCV** – Real-time computer vision
* **TensorFlow** – Deep learning framework for gesture model
* **MediaPipe** – Hand tracking and gesture recognition
* **HTML/CSS** – Frontend interface
* **Pretrained model:** `gesture_model.h5`

---

## 📁 Folder Structure

```
Touchless_Interaction_With_Kisok/
│
├── app.py                      # Main backend script
├── gesture_model.h5            # Trained gesture model
├── index111.html               # HTML UI
│
├── static/                     # Assets (images, styles)
│   ├── *.png                   # Icon images
│   ├── *.jpg                   # Background/check-in images
│   ├── styles.css              # Styling
│   ├── styles1.css
│   └── styles2.css
```

---

## 📦 requirements.txt

```txt
Flask
opencv-python
tensorflow
mediapipe
numpy
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes

```bash
git commit -m "Add some AmazingFeature"
```

4. Push to your branch

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

