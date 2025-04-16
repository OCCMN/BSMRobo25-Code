import cv2

# Open connections to the two cameras (0 and 1)
cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)


# Check if both cameras are opened
if not cap1.isOpened():
    print("Error: Could not open camera 1.")
    exit()
if not cap2.isOpened():
    print("Error: Could not open camera 2.")
    exit()

    
# Set desired width and height for both cameras (e.g., 1280x720)
width = 800
height = 600
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# Set the desired frame rate 
fps = 15
cap1.set(cv2.CAP_PROP_FPS, fps)
cap2.set(cv2.CAP_PROP_FPS, fps)

while True:
    # Read frames from both cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    
        # Display the frames from both cameras
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)
   
    
    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the cameras and close all windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()
