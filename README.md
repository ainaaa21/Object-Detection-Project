# 🛠️ **Real-Time Defect Detection and Classification for Canned Food Packaging**

🚀 **Exploring AI in Quality Control**

This project demonstrates the practical application of **AI, deep learning, and computer vision** to automate quality control in manufacturing. It focuses on **real-time defect detection in canned food packaging**, using **YOLOv8 by Ultralytics, OpenCV, and Flask** to simulate an automated inspection system.

---

## ❌ Problem Statement

Manual inspection of canned packaging is:  
- Time-consuming ⏳  
- Prone to human error 😵  
- Inconsistent in quality ✅/❌  
- Traditional image processing methods lack real-time accuracy  

👉 Defects such as **dents, leaks, or punctures** can compromise food safety and lead to product recalls. 

---

## 💡 Proposed Solution

Build a **real-time defect detection and classification system** that:  
- Automates inspection using **computer vision + deep learning**  
- Detects and classifies dents as **major, minor, or no defect**, specifically **dent defect** used for this project 
- Provides instant feedback through a simple **Flask web app**  
- Simulates integration into a production line  

---

## 📊 Dataset & Preparation

- **Source:** 900 images of canned packaging (3 classes: major, minor, no defect). Below are examples of sample dataset used in this project:
<p align="center">
  <img src="user interface/Major Defect.png" alt="Major Defect" width="150" height="200"/>
  <img src="user interface/Minor Defect.png" alt="Minor Defect" width="150" height="148"/>
  <img src="user interface/No Defect.png" alt="No Defect" width="150" height="148"/>
</p>

- **Tool:** Roboflow for annotation, resizing, and augmentation  
- **Final Dataset:** 1,292 images after preprocessing  
- **Split:** 70% training, 20% validation, 10% testing  

---

## 🤖 Model Training & Evaluation

- Trained multiple YOLOv8 variants (n, s, m, l)  
- Results: All achieved **99.5% mAP**  
- Chosen model: **YOLOv8n** (nano) → best tradeoff between speed & accuracy  
  - Latency: 5.7 ms/frame  
  - Parameters: 30.06M  
  - Accuracy: **96.7% overall**  
    - 100% for *major* and *minor defects*  
    - 90% for *no defect*  

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

## 🎥 Demo (Optional)

<p align="center">
  <img src="docs/demo.gif" alt="Live Detection Demo" width="600"/>
</p>

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

## 📌 Limitations & Future Work

- Dataset only covers **silver tall cans** → expand to different colors and materials  
- Sensitive to **lighting conditions** → improve preprocessing and augmentation  
- Future directions:  
  - Experiment with **YOLOv11** and advanced optimizers  
  - Simulate more realistic **factory environments**  
  - Add dashboard for **defect logging and analytics**
    
---

## 💬 Learning Outcomes

🔹 Gained **hands-on experience** with YOLOv8 object detection  
🔹 Applied **computer vision** in a manufacturing context  
🔹 Built a working **end-to-end prototype** with Flask  
🔹 Learned to balance **accuracy vs speed** for real-time AI  
🔹 Developed **problem-solving & adaptability** skills  
