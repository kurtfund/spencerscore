import cv2
import os

video_path = "uploads/hf_20260421_182949_fff9ea9a-8fd4-4a7f-9b88-7c76a5e96e04.mp4"
output_dir = "uploads/hero_frames"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Opening video {video_path}...")
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit(1)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Total frames: {frame_count}, FPS: {fps}")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save frame as JPEG
    # Zero-pad filename to 4 digits for easy sorting (e.g., 0001.jpg, 0002.jpg)
    out_path = os.path.join(output_dir, f"frame_{count:04d}.jpg")
    
    # Optional: resize to save memory if video is huge
    # frame = cv2.resize(frame, (1280, 720))
    
    cv2.imwrite(out_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    count += 1
    
    if count % 20 == 0:
        print(f"Extracted {count}/{frame_count} frames...")

cap.release()
print(f"Done! Extracted {count} frames to {output_dir}")
