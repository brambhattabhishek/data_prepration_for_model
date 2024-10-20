import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess an image for CNN input.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - np.ndarray: Preprocessed image ready for CNN input.
    
    Raises:
    - ValueError: If the image cannot be loaded.
    """
    
    # Load the image
    img = cv2.imread(image_path)

    # Check if the image is loaded properly
    if img is None:
        raise ValueError(f"Image not found or unable to load: {image_path}")

    # Convert to grayscale (optional, uncomment if needed)
    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize image to match the input size of the CNN model
    resized_img = cv2.resize(img, (224, 224))  # Adjust size based on your model requirements

    # Normalize the image (optional but recommended for CNNs)
    normalized_img = resized_img.astype(np.float32) / 255.0

    # If the CNN model expects a batch of images, expand dimensions
    preprocessed_img = np.expand_dims(normalized_img, axis=0)

    return preprocessed_img

# Example usage
if __name__ == "__main__":
    image_path = 'path/to/your/image.jpg'  # Replace with your actual image path
    try:
        preprocessed_image = preprocess_image(image_path)
        print("Image preprocessed successfully.")
        print(preprocessed_image.shape)  # Display the shape of the preprocessed image
    except ValueError as e:
        print(e)
