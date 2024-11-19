import numpy as np
import os
from PIL import Image
import cv2
from sklearn.decomposition import PCA

# Step 1: Load and preprocess the images
def load_images(image_dir):
    image_data = []
    labels = []
    image_paths = os.listdir(image_dir)
    
    for i, image_name in enumerate(image_paths):
        img_path = os.path.join(image_dir, image_name)
        img = Image.open(img_path).convert("L")  
        img = img.resize((100, 100)) 
        img_array = np.array(img).flatten()  
        image_data.append(img_array)
        labels.append(i)  
    
    return np.array(image_data), np.array(labels)

# Step 2: Perform PCA to extract the principal components
def apply_pca(image_data, num_components=50):
    pca = PCA(n_components=num_components)
    pca.fit(image_data)
    return pca

# Step 3: Compare faces using Euclidean distance
def recognize_face(pca, face_data, input_face):
    # Project the input face into PCA space
    input_face_pca = pca.transform([input_face])
    
    # Compare the input face with stored faces using Euclidean distance
    distances = np.linalg.norm(face_data - input_face_pca, axis=1)
    
    # Find the index of the closest match
    closest_face_idx = np.argmin(distances)
    
    return closest_face_idx, distances[closest_face_idx]

# Step 4: Capture live webcam feed
def capture_and_recognize_face(image_dir, pca):
    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the image to match the training images
        resized_gray = cv2.resize(gray, (100, 100))

        # Flatten the resized image
        flattened_face = resized_gray.flatten()

        # Compare the live frame's face with the stored faces
        face_data, _ = load_images(image_dir)  # Load the training data
        face_data = pca.transform(face_data)   # Project the training faces to PCA space

        closest_face_idx, distance = recognize_face(pca, face_data, flattened_face)

        # Draw a red rectangle around the face in the frame
        if distance < 100:  # Set a threshold distance for matching (adjust as needed)
            print(f"Recognized face at index {closest_face_idx} with distance {distance}")
            x, y, w, h = 50, 50, 100, 100  # Example coordinates (use a face detector if needed)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw red rectangle

        # Display the resulting frame
        cv2.imshow("Face Recognition", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
# Assuming you have a folder "captured_faces/" containing the 100 face images.
image_directory = "data/"

# Load and apply PCA to the training data
image_data, _ = load_images(image_directory)
pca = apply_pca(image_data)

# Start capturing the webcam feed and recognizing faces
capture_and_recognize_face(image_directory, pca)
