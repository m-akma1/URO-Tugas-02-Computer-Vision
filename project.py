import cv2
import numpy as np

# Load the video
video_source = cv2.VideoCapture('object_video.mp4')

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

    # Display the frame with detected object(s)
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video and destroy all windows
video_source.release()
cv2.destroyAllWindows()
