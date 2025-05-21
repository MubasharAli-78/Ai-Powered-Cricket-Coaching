# from ultralytics import YOLO
# import numpy as np
# import cv2
# Load the YOLOv8 model
# model = YOLO('yolov8x.pt')

#
# def process_video(video_path):
#     """
#     Process the video to find the frame where the bat and ball are closest,
#     analyzing only every 10th frame per 60 fps for optimization.
#
#     :param video_path: Path to the input video.
#     :return: Angle analysis on the best frame.
#     """
#     cap = cv2.VideoCapture(video_path)
#
#     if not cap.isOpened():
#         print(f"Error: Unable to open video at path '{video_path}'")
#         return None
#
#     fps = int(cap.get(cv2.CAP_PROP_FPS))  # Typically 60
#     frames_to_skip = int(fps / 6)  # Process 6 frames per second
#
#     min_distance = float('inf')
#     best_frame = None
#     best_bat_center = None
#     frame_count = 0
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         frame_count += 1
#
#         # Skip frames to reduce processing
#         if frame_count % frames_to_skip != 0:
#             continue
#
#         results = model(frame)
#         bat_center, ball_center = None, None
#
#         for result in results:
#             for box in result.boxes:
#                 class_id = int(box.cls[0])
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
#
#                 if class_id == 34:  # Bat
#                     bat_center = (center_x, center_y)
#                     cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
#                     cv2.circle(frame, bat_center, 5, (255, 0, 0), -1)
#                     cv2.putText(frame, "Bat", (x1, y1 - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
#
#                 elif class_id == 32:  # Ball
#                     ball_center = (center_x, center_y)
#                     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.circle(frame, ball_center, 5, (0, 255, 0), -1)
#                     cv2.putText(frame, "Ball", (x1, y1 - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#         if bat_center and ball_center:
#             distance = np.linalg.norm(np.array(bat_center) - np.array(ball_center))
#             cv2.putText(frame, f"Distance: {distance:.2f}", (10, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
#
#             if distance < min_distance:
#                 min_distance = distance
#                 best_frame = frame.copy()
#                 best_bat_center = bat_center
#
#         cv2.imshow("Tracking Bat and Ball", frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#     if best_frame is not None:
#         print(f"Best frame found after processing {frame_count} frames.")
#         print(f"Bat center at closest approach: {best_bat_center}")
#         # cv2.imshow("img", img)
#         cv2.imshow("best_frame", best_frame)
#         cv2.waitKey(0)
#         return best_frame, best_bat_center
#     else:
#         print("No frame with both bat and ball detected.")
#         return None
#

# all_angles, result_img = process_video(r'Videos\Clip 1.mp4')
# angles = processing_image(image)
# print("✅ Calculated Angles:", all_angles)
# cv2.imshow("result_img", result_img)
# cv2.waitKey(0)
# Example usage
# video_path = r"./videos/Babar Azam Best Cover Drives.mp4"  # Replace with your input video path
# best_frame = process_video(video_path)
#
# if best_frame is not None:
#     # Save or process the best frame further
#     output_image_path = r"best_frame.jpg"
#     cv2.imwrite(output_image_path, best_frame)
#     print(f"Best frame saved as {output_image_path}.")
# else:
#     print("No suitable frame found.")