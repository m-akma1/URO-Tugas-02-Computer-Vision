import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('object_video.mp4')

# Loop through each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the HSV color range for the object to be detected
    lower_color = np.array([30, 150, 50])
    upper_color = np.array([255, 255, 180])

    # Generate the HSV mask
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Apply mask to the original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours from the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour to draw bounding rectangles
    for contour in contours:
        area = cv2.contourArea(contour)
        # Filtering objects based on contour area (example: area > 500 to avoid noise)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected object(s)
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video and destroy all windows
cap.release()
cv2.destroyAllWindows()
