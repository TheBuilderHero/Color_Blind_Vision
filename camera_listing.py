import cv2

def list_cameras():
    # Attempt to find available cameras
    camera_indices = []
    for index in range(10):  # Check for up to 10 camera indices
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            camera_indices.append(index)
            cap.release()
    return camera_indices

def open_camera(camera_index):
    cam = cv2.VideoCapture(camera_index)
    if not cam.isOpened():
        print(f"Camera at index {camera_index} could not be opened.")
        return None
    return cam

def main():
    camera_indices = list_cameras()
    if not camera_indices:
        print("No cameras found.")
        return

    print("Available cameras:")
    for idx in camera_indices:
        print(f"Camera index: {idx}")

    # Allow user to select the camera
    selected_index = int(input("Select a camera index: "))
    if selected_index not in camera_indices:
        print("Invalid camera index selected.")
        return

    cam = open_camera(selected_index)
    if cam is None:
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to capture frame.")
            break
        
        cv2.imshow(f'Camera {selected_index}', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
