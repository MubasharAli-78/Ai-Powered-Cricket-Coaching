# 🏏 AI-Powered Gesture-Based Cricket Coaching System

**A next-generation cricket coaching platform by Mubashar Ali that leverages computer vision and deep learning to provide real-time posture tracking, gesture recognition, angle analysis, and in-depth performance analytics — all with instant feedback to elevate players’ skills.**

---

![Poster Preview](images/Poster.png)

---

## 🚀 Key Features

- **🎯 Real-time Gesture Recognition**  
  Detect batting and bowling postures with YOLOv8 and MediaPipe for instant gesture identification.

- **📐 Angle & Biomechanical Analysis**  
  Compute key joint and bat-swing angles (elbow, shoulder alignment) to optimize technique and reduce injury risk.

- **⚡ Instant Feedback Engine**  
  Visual and textual cues during practice sessions highlight posture deviations and suggest corrective drills.

- **🎥 Session Recording & Annotated Review**  
  High-resolution video capture with overlaid skeletons and performance metrics for post-session analysis.

- **📊 Performance Dashboard**  
  Interactive charts and tables to track progress over time, benchmark against goals, and export reports.

---

## 🎯 Main Objectives

1. **Enhance Coaching Efficiency**  
   Automate posture and gesture analysis so coaches can focus on strategy rather than manual review.

2. **Improve Player Technique**  
   Use quantitative angle metrics and biomechanical comparisons to refine batting and bowling form.

3. **Data-Driven Progress Tracking**  
   Empower coaches and players to visualize skill development and pinpoint areas for improvement.

---

## 🛠️ Tech Stack & Tools

- **Backend & Data**  
  - Python 3.10, Flask, OpenCV, NumPy  
  - SQL Server for session metadata and analytics

- **Computer Vision & ML**  
  - PyTorch, YOLOv8 for detection  
  - MediaPipe for pose estimation  
  - Custom CNNs for posture classification

- **Frontend (Flutter)**  
  - Dart, Material UI widgets, animations  
  - Responsive layouts for Android & iOS

- **Visualization & Dashboard**  
  - React + Tailwind CSS (web)  
  - Chart.js / Recharts for graphs

- **Development Environments**  
  - VS Code, PyCharm, Android Studio, Xcode

---

## 🏗️ System Architecture

```text
Camera Input
    ↓
[Preprocessing]
    ↓
[YOLOv8 & MediaPipe] → Keypoint Extraction
    ↓
[Angle Computation]
    ↓
[Feedback Engine]
    ↓
[Session Recording + Overlay]
    ↓
[Analytics & Dashboard]
