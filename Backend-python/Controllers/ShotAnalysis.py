from flask import Flask, request, jsonify
import cv2
import numpy as np
import os
from ultralytics import YOLO
import mediapipe as mp
import datetime

app = Flask(__name__)

model = YOLO(r'C:\Users\MUBASHAR\PycharmProjects\CricketCoach\Controllers\yolov8x.pt')

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return angle if angle <= 180.0 else 360 - angle

JOINT_COLOR = (255, 0, 255)
LINE_COLOR = (255, 0, 0)

important_joints = {
    "Left Shoulder": 11, "Right Shoulder": 12,
    "Left Elbow": 13, "Right Elbow": 14,
    "Left Wrist": 15, "Right Wrist": 16,
    "Left Hip": 23, "Right Hip": 24,
    "Left Knee": 25, "Right Knee": 26,
    "Left Ankle": 27, "Right Ankle": 28,
    "Left Toe": 29, "Right Toe": 30, "Left Heel": 31, "Right Heel": 32
}

angle_connections = {
    "Left Elbow": (11, 13, 15),
    "Right Elbow": (12, 14, 16),
    "Left Knee": (23, 25, 27),
    "Right Knee": (24, 26, 28),
    "Left Shoulder": (23, 11, 13),
    "Right Shoulder": (24, 12, 14),
    "Left Hip": (11, 23, 25),
    "Right Hip": (12, 24, 26),
    "Left Toe": (25, 27, 29),
    "Right Toe": (26, 28, 30),
    "Left Heel": (25, 27, 31),
    "Right Heel": (26, 28, 32)
}

def draw_all_joints(image, landmarks):
    h, w, _ = image.shape
    for joint_name, idx in important_joints.items():
        landmark = landmarks[idx]
        cx, cy = int(landmark.x * w), int(landmark.y * h)
        cv2.circle(image, (cx, cy), 8, JOINT_COLOR, -1)

def draw_connections(image, landmarks):
    h, w, _ = image.shape
    for connection_name, (start_idx, mid_idx, end_idx) in angle_connections.items():
        start_point = landmarks[start_idx]
        mid_point = landmarks[mid_idx]
        end_point = landmarks[end_idx]

        start_pos = (int(start_point.x * w), int(start_point.y * h))
        mid_pos = (int(mid_point.x * w), int(mid_point.y * h))
        end_pos = (int(end_point.x * w), int(end_point.y * h))

        cv2.line(image, start_pos, mid_pos, LINE_COLOR, 3)
        cv2.line(image, mid_pos, end_pos, LINE_COLOR, 3)

def draw_angles(image, landmarks):
    h, w, _ = image.shape
    text_y = 30
    angles = {}
    for angle_name, (p1, p2, p3) in angle_connections.items():
        point1 = landmarks[p1]
        point2 = landmarks[p2]
        point3 = landmarks[p3]

        p1_coords = [point1.x * w, point1.y * h]
        p2_coords = [point2.x * w, point2.y * h]
        p3_coords = [point3.x * w, point3.y * h]

        angle = calculate_angle(p1_coords, p2_coords, p3_coords)

        # cv2.putText(image,
        #             f"{angle_name}: {int(angle)}°",
        #             (10, text_y),
        #             cv2.FONT_HERSHEY_SIMPLEX,
        #             0.6,
        #             TEXT_COLOR,
        #             2,
        #             cv2.LINE_AA)
        # text_y += 25

        angles[angle_name] = {
            "angle": angle,
            "points": {
                "p1": p1_coords,
                "p2": p2_coords,
                "p3": p3_coords
            }
        }

    return angles

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image_path = 'uploaded_image.jpg'
    image_file.save(image_path)

    image = cv2.imread(image_path)
    if image is None:
        return jsonify({'error': 'Invalid image file'}), 400


    results = model(image)
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            if class_id in [32, 34]:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                color = (0, 0, 255) if class_id == 32 else (0, 255, 0)
                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)


    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_tracking_confidence=0.5, static_image_mode=True)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_image)

    if not results.pose_landmarks:
        return jsonify({'error': 'No pose landmarks detected'}), 400

    landmarks = results.pose_landmarks.landmark


    draw_all_joints(image, landmarks)
    draw_connections(image, landmarks)
    angles = draw_angles(image, landmarks)


    specific_angles = {
        "Left Arm": angles.get("Left Elbow", {}).get("angle", "Not Detected"),
        "Left Leg": angles.get("Left Knee", {}).get("angle", "Not Detected"),
        "Right Arm": angles.get("Right Elbow", {}).get("angle", "Not Detected"),
        "Right Leg": angles.get("Right Knee", {}).get("angle", "Not Detected")
    }


    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = 'images'
    os.makedirs(output_dir, exist_ok=True)
    output_image_path = os.path.join(output_dir, f'processed_{timestamp}.jpg')
    cv2.imwrite(output_image_path, image)

    return jsonify({
        'message': 'Successfully Shot Analysis  Performed',
        'output_image': output_image_path,
        'angles': specific_angles
    })

if __name__ == "__main__":
    app.run(debug=True)