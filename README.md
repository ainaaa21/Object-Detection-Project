# 🛠️ **Real-Time Defect Detection and Classification for Canned Food Packaging**

🚀 **Exploring AI in Quality Control**

This is a project developed to demonstrate a practical understanding of **AI, deep learning, and computer vision** by building a prototype for **real-time defect detection in canned food packaging**. Leveraging **YOLOv8 by Ultralytics and OpenCV**, the system simulates an automated quality control process—showcasing the potential of AI in manufacturing and inspection tasks.  

---

## 🔍 Project Objectives

✅ **Hands-On Deep Learning** – Apply object detection techniques to a real-world use case.  
✅ **Real-Time Processing** – Demonstrate the ability to detect and classify defects instantly.  
✅ **Practical Application Focus** – Tailored for packaging defects like dents, scratches, and deformations.  
✅ **Web Deployment Simulation** – Use Flask to simulate deployment in a production-like environment.

---

## 🌟 Key Features

🔹 **Real-Time Detection** – Simulates live detection using a webcam or video input.  
🔹 **Packaging-Specific Use Case** – Focused on identifying visual defects in canned goods.  
🔹 **YOLOv8 Accuracy** – Utilizes a state-of-the-art model for reliable object detection.  
🔹 **Streamlined Processing** – Processes frames efficiently using OpenCV.  
🔹 **Web Interface** – Basic UI built with Flask to visualize results and mimic real-world deployment.

---
## 🖥️ Sample Web Interface

Below is the user interface for the SmartDetection system:

### 🔹 Home Page  
<p align="center">
  <img src="user interface/interface1.png" alt="SmartDetection Home Interface" width="700"/>
</p>

> 📷 Users are greeted with a simple welcome screen and a clickable camera icon to start detection.

### 🔹 Live Detection in Action  
<p align="center">
  <img src="user interface/interface2.png" alt="Real-Time Detection Interface" width="700"/>
</p>

> 🛠️ Once detection begins, users receive real-time feedback with bounding boxes and confidence scores. Instructions and defect status are clearly shown for user guidance.

---

## ⚙️ Tech Stack & Dependencies

📌 **Programming Language:** Python 🐍  
📌 **Deep Learning Framework:** [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) 🤖  
📌 **Computer Vision Library:** OpenCV 👀  
📌 **Web Framework:** Flask 🌍  

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
## ⚙️ How It Works

1️⃣ **Captures** live video input.  
2️⃣ **Processes** frames using OpenCV.  
3️⃣ **Runs** object detection using YOLOv8.  
4️⃣ **Displays** results via Flask web interface.

---
## 💬 Learning Outcomes

🔹 Gained **hands-on experience** with YOLOv8 object detection.  
🔹 Applied **computer vision techniques** in a manufacturing context.  
🔹 Explored **real-time AI deployment** using Flask.
