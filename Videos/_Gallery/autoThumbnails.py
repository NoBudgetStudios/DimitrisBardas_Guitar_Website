import cv2
import glob
import random
import os

# Path to search for mp4 files - adjust this as needed
search_path = "./*.mp4"

# Function to extract a random frame from a video
def extract_random_frame(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file {video_path}")
        return
    
    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Choose a random frame
    random_frame_number = random.randint(0, total_frames - 1)
    
    # Set the current frame position of the video file to the random frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)
    
    # Read the frame
    success, frame = cap.read()
    if success:
        # Construct output image path
        base_name = os.path.basename(video_path)
        image_name = "thumbnail "+os.path.splitext(base_name)[0].split(" ")[1]+".jpg"
        # Save the frame as a JPG file
        cv2.imwrite(image_name, frame)
        print(f"Extracted frame from {video_path} to {image_name}")
    else:
        print(f"Failed to extract frame from {video_path}")
    
    # Release the video capture object
    cap.release()

# Find all mp4 files in the directory
mp4_files = glob.glob(search_path)

# Extract a random frame from each mp4 file
for video_path in mp4_files:
    extract_random_frame(video_path)
