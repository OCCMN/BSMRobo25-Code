import cv2

# Open a connection to the first camera (0 is the default camera)

cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the desired frame width and height (aspect ratio 16:9)
width = 800
height = 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Set the desired frame rate (30 FPS)
fps = 15
cap.set(cv2.CAP_PROP_FPS, fps)

# Check if the settings are applied correctly
actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
actual_fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Actual Width: {actual_width}, Actual Height: {actual_height}, Actual FPS: {actual_fps}")

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # If a frame was read successfully, display it
    if ret:
        cv2.imshow("Camera", frame)
    else:
        print("Error: Failed to grab frame.")
        break
    
    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()