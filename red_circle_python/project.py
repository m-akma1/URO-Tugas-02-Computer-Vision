import cv2
import numpy as np

# Load the video
video_source = cv2.VideoCapture('object_video.mp4')

# Define the codec and create VideoWriters for output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_frame = cv2.VideoWriter('output_frame.avi', fourcc, 20.0, (int(video_source.get(3)), int(video_source.get(4))))
out_mask = cv2.VideoWriter('output_mask.avi', fourcc, 20.0, (int(video_source.get(3)), int(video_source.get(4))))

# Create resizable windows
cv2.namedWindow('Detected Object', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detected Object', 640 , 360)
cv2.namedWindow('Masked Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Masked Video', 640 , 360)
cv2.moveWindow('Detected Object', 20, 100)
cv2.moveWindow('Masked Video', 720, 100)

# Loop through each frame
while True:
    ret, frame = video_source.read()
    if not ret:
        break

    # Convert the frame to HSV
    hsv_converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the HSV color range for the red object to be detected
    low_bound_1 = np.array([0, 120, 70])
    up_bound_1 = np.array([10, 255, 255])
    
    low_bound_2 = np.array([170, 120, 70])
    up_bound_2 = np.array([180, 255, 255])
    
    # Generate the HSV mask for both red ranges
    mask1 = cv2.inRange(hsv_converted_frame, low_bound_1, up_bound_1)
    mask2 = cv2.inRange(hsv_converted_frame, low_bound_2, up_bound_2)
    
    # Combine both masks
    mask = cv2.bitwise_or(mask1, mask2)

    # Apply mask to the original frame
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours from the mask
    detected_contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour to draw bounding rectangles
    for contour in detected_contours:
        area = cv2.contourArea(contour)
        # Filtering objects based on contour area (example: area > 100 to avoid noise)
        if area > 100:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Write the processed frames to the output videos
    out_frame.write(frame)
    out_mask_frame = cv2.merge([mask, mask, mask])  # Convert mask to 3-channel to save as video
    out_mask.write(out_mask_frame)

    # Add custom overlay text
    cv2.putText(frame, 'Press Q to Quit', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Detected Objects: {len(detected_contours)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    progress = int((video_source.get(cv2.CAP_PROP_POS_FRAMES) / video_source.get(cv2.CAP_PROP_FRAME_COUNT)) * 100)
    cv2.putText(frame, f'Progress: {progress}%', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the frame with detected object(s)
    cv2.imshow('Detected Object', frame)
    cv2.imshow('Masked Video', mask)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video and destroy all windows
video_source.release()
out_frame.release()
out_mask.release()
cv2.destroyAllWindows()
