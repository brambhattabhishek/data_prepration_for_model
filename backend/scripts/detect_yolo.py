from inference_sdk import InferenceHTTPClient

# Set up the InferenceHTTPClient with your Roboflow API URL and API key
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="TenTAUZM2pf9NlkWlcMA"  # Your provided API key
)

def yolo_inference(image_path):
    # Specify the model ID you want to use
    model_id = "freshness-detection-rhrze/3"  # Replace with your actual model ID

    # Make a prediction using the infer method
    result = CLIENT.infer(image_path, model_id=model_id)

    # Initialize the structured response
    structured_response = {
        'status': result.get('status', 'unknown'),
        'message': result.get('message', 'No message provided'),
        'results': {
            'category': 'unknown',
            'items': []
        }
    }

    # Check if there are predictions in the result
    if 'predictions' in result:
        detected_items = []

        # Iterate over the predictions and gather information
        for prediction in result['predictions']:
            label = prediction.get('class', 'unknown')  # Getting the class name
            confidence = prediction.get('confidence', 0.0)  # Confidence score
            bbox = prediction.get('bbox', [0, 0, 0, 0])  # Bounding box coordinates

            detected_items.append({
                'label': label,
                'confidence': confidence,
                'bounding_box': bbox  # Directly using bbox from predictions
            })

        # Set the category based on detected items
        if any(item['label'] == 'apple' for item in detected_items):
            structured_response['results']['category'] = 'fruits_vegetables'
        else:
            structured_response['results']['category'] = 'packaged_goods'
        
        # Add the detected items to the response
        structured_response['results']['items'] = detected_items

    return structured_response

# Example usage
if __name__ == "__main__":
    image_path = 'path/to/your/image.jpg'  # Replace with your image path
    result = yolo_inference(image_path)
    print(result)
