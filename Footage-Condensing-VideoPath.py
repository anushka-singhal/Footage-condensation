import cv2

# Set input and output file paths
input_path = "video1.mp4"
output_path = "video1_output_video.avi"

# Set target duration and fps
target_duration = int(input("Enter a duration in seconds: "))  # seconds
target_fps = int(input("Enter FPS: "))
print("FPS : ",target_fps)

# Open input video file
input_video = cv2.VideoCapture(input_path)

# Get input video properties
frame_count = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))
length_in_secs = frame_count / fps
print("Length in secs : ",length_in_secs)

# Calculate skip frames interval
skip_frames_interval = int((frame_count / target_duration) / target_fps) # avg fps divide by target frames

# Get input video frame size
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create output video file
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_video = cv2.VideoWriter(output_path, fourcc, target_fps, (frame_width, frame_height), isColor=False)

# Process video frames and write to output file
frame_number = 0
while True:
    # Read a frame from the input video
    ret, frame = input_video.read()

    # If the frame could not be read, break the loop
    if not ret:
        break

    # Apply a grayscale conversion to the frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the processed frame to the output video
    if frame_number % skip_frames_interval == 0:
        output_video.write(gray_frame)

    # Increment the frame number
    frame_number += 1

# Release video objects
input_video.release()
output_video.release()

# Print output video duration
print(f"Input video duration: {length_in_secs} seconds")
print(f"Output video duration: {target_duration} seconds")

