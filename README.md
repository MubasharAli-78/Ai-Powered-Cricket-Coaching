# AI-Powered Gesture-Based Cricket Coaching System

**A next-generation cricket coaching platform that leverages computer vision and deep learning to provide real-time posture tracking, gesture recognition, angle analysis, and in-depth performance analytics — all with instant feedback to elevate players’ skills.**

---

## 🚀 Key Features

- **Real-time Gesture Recognition**  
  Detects batting and bowling postures using advanced deep-learning models (e.g., YOLOv8, MediaPipe) to identify key gestures and movements on the fly.

- **Angle Calculation & Biomechanical Analysis**  
  Computes joint and bat-angle metrics (e.g., elbow flexion, shoulder alignment) to ensure optimal technique and prevent injury.

- **Instant Feedback & Coaching Tips**  
  Provides visual and textual feedback during practice sessions, highlighting posture deviations and suggesting corrective drills.

- **Session Recording & Review**  
  Records every training session in high-resolution video, annotated with overlayed skeletons and key performance metrics for post-practice analysis.

- **Comprehensive Performance Dashboard**  
  Aggregates session data into graphs and tables to track progress over time, compare against benchmarks, and set personalized goals.

---

## 🎯 Main Objectives

1. **Enhance Coaching Efficiency**  
   Automate posture and gesture analysis so coaches can focus on personalized training strategies rather than manual video review.

2. **Improve Player Technique**  
   Use quantitative angle measurements and biomechanical comparisons to fine-tune batting and bowling form.

3. **Data-Driven Progress Tracking**  
   Enable both coaches and players to visualize improvements and identify areas needing attention through detailed analytics.

---

## 🛠️ Tech Stack & Tools

- **Backend & Data**:  
  - Python 3.10, OpenCV, NumPy  
  - SQL Server for session metadata and analytics storage

- **Computer Vision & ML**:  
  - PyTorch, YOLOv8 for object/gesture detection  
  - MediaPipe for skeletal tracking  
  - Custom CNNs for fine-grained posture classification

- **Frontend & Visualization**:  
  - React (with Tailwind CSS) for interactive dashboards  
  - Chart.js / Recharts for performance graphs

- **Development Environments**:  
  - VS Code, PyCharm, Android Studio, Xcode

---

## 🏗️ System Architecture

1. **Data Ingestion**  
   - High-fps camera input → frame extraction  
   - Preprocessing (normalization, cropping)

2. **Gesture & Pose Estimation**  
   - YOLOv8 detection → bounding boxes  
   - MediaPipe skeleton overlay → key-point extraction

3. **Angle Computation**  
   - Vector math on joint coordinates → angle metrics

4. **Feedback Engine**  
   - Rule-based and ML-driven recommendations  
   - Overlay highlights on video frames

5. **Analytics & Dashboard**  
   - SQL queries → metrics aggregation  
   - Frontend visualizations & reports

---

## 👥 Team & Supervision

- **Developed By:**  
  - Mubashar Ali (21-ARID-4482)  
  - M. Aneeq (21-ARID-4499)  
  - Awais Ahmad (21-ARID-4415)  
  - Talal Waheed (21-ARID-4611)

- **Supervised By:**  
  Dr. Hassan Nazeer

---

## 📂 Repository Structure

