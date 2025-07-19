# 🛠️ **Real-Time Defect Detection and Classification for Canned Food Packaging**

🚀 **Exploring AI in Quality Control**

This is a project developed to demonstrate a practical understanding of **AI, deep learning, and computer vision** by building a prototype for **real-time defect detection in canned food packaging**. Leveraging **YOLOv8 by Ultralytics and OpenCV**, the system simulates an automated quality control process—showcasing the potential of AI in manufacturing and inspection tasks.  

---

## 🔍 Project Objectives

✅ **Hands-On Deep Learning** – Applied object detection to identify dents in canned packaging.  
✅ **Real-Time Defect Classification** – Detected and classified dents into three levels: **major**, **minor**, and **no defect** instantly.  
✅ **Packaging-Focused Application** – Designed specifically for quality control in canned food packaging.  
✅ **Web Deployment Simulation** – Used Flask to simulate a live production environment for real-time monitoring.

---
## ⚙️ Tech Stack & Dependencies

📌 **Programming Language:** Python 🐍  
📌 **Deep Learning Framework:** [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) 🤖  
📌 **Computer Vision Library:** OpenCV 👀  
📌 **Web Framework:** Flask 🌍  

---

## ⚙️ How It Works

1️⃣ **OpenCV captures video**  
The system uses OpenCV to access your webcam and capture video frames in real-time.

2️⃣ **Frames sent to YOLOv8 model**  
Each frame is passed to the YOLOv8 model to detect defects on the can (like dents).  

3️⃣ **Results added to frame**  
YOLOv8 returns the detection results (boxes, labels, confidence), and OpenCV draws them on the video.

4️⃣ **Flask shows the video in browser**  
The final video with defect info is displayed live on a simple web page using Flask.

---
## 🖥️ Sample Web Interface

Below is the user interface for the SmartDetection system:

### 🔹 Home Page  
<p align="center">
  <img src="user interface/interface1.png" alt="SmartDetection Home Interface" width="500"/>
</p>

> 📷 Users are greeted with a simple welcome screen and a clickable camera icon to start detection.

### 🔹 Live Detection in Action  
<p align="center">
  <img src="user interface/interface2.png" alt="Real-Time Detection Interface" width="500"/>
</p>

> 🛠️ Once detection begins, users receive real-time feedback with bounding boxes and confidence scores. Instructions and defect status are clearly shown for user guidance.

---

## 🚀 Getting Started

### 🔧 **1. Clone the Repository**
```bash
git clone https://github.com/ainaaa21/Object-Detection-Project.git
cd Object-Detection-Project
```

### 📦 **2. Install Dependencies**  
```bash
pip install opencv-python ultralytics flask flask_socketio
```

### 🚀 **3. Run the Application**  
```bash
python app.py
```
Once started, the system will analyze incoming frames and detect packaging defects in real-time! 🏭✨  

---

## 💬 Learning Outcomes

🔹 Gained **hands-on experience** with YOLOv8 object detection.  
🔹 Applied **computer vision techniques** in a manufacturing context.  
🔹 Explored **real-time AI deployment** using Flask.
