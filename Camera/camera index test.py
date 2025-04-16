import cv2

def test_camera(index):
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print(f"Error: Camera {index} could not be opened.")
    else:
        print(f"Camera {index} is available.")
    cap.release()

# Test for camera indices from 0 to 3
for i in range(4):  # Change range if you have more than 4 cameras
    test_camera(i)
