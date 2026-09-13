import cv2
import os

# 1. Create a folder to save images if it doesn't exist
folder_name = "captured_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")

# 2. Initialize the camera (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Instructions:")
print("- Press 's' to save an image")
print("- Press 'q' to quit")

img_counter = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the resulting frame
    cv2.imshow('Camera Feed - Press S to Save', frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        # Quit the program
        print("Closing program...")
        break
    
    elif key == ord('s'):
        # Save the current frame as an image
        img_name = os.path.join(folder_name, f"image_{img_counter}.png")
        cv2.imwrite(img_name, frame)
        print(f"Saved: {img_name}")
        img_counter += 1

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
