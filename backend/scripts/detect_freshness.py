from tensorflow.keras.models import load_model
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template
import base64
import os
import matplotlib.pyplot as plt
from io import BytesIO

# Initialize Flask app
app = Flask(__name__)

# Load your trained Keras model
model_path = r'C:/Users/Hp/OneDrive/Desktop/Full_Projects_Flipkart_Grid/backend/models/best_model.keras'
model = load_model(model_path)  # Load the model from the specified path

def cnn_freshness_inference(image_path):
    # Preprocess the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or could not be loaded.")

    img = cv2.resize(img, (224, 224))  # Resize to match input size for the CNN model
    img = img / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)

    # Run inference
    freshness_score = model.predict(img)[0]

    # Check for valid output
    if len(freshness_score) != 7:
        raise ValueError(f"Model output does not have the expected number of indices. Got {len(freshness_score)} instead.")

    # Extracting indices from the predicted scores
    freshness_index = freshness_score[0] if not np.isnan(freshness_score[0]) else 0
    ripeness_stage_index = freshness_score[1] if not np.isnan(freshness_score[1]) else 0
    size_index = freshness_score[2] if not np.isnan(freshness_score[2]) else 0
    color_index = freshness_score[3] if not np.isnan(freshness_score[3]) else 0
    nutrition_index = freshness_score[4] if not np.isnan(freshness_score[4]) else 0
    weight_index = freshness_score[5] if not np.isnan(freshness_score[5]) else 0
    lifespan_score = freshness_score[6] if not np.isnan(freshness_score[6]) else 0

    # Normalize the freshness index to a percentage
    freshness_percentage = (freshness_index / 10.0) * 100 if freshness_index is not None else 0

    # Construct structured output
    structured_output = {
        'status': 'success',
        'name': 'Fruit/Vegetable Name',  # Placeholder for the actual name
        'freshness_percentage': freshness_percentage,
        'ripeness_stage_index': ripeness_stage_index,
        'size_index': size_index,
        'color_index': color_index,
        'nutrition_index': nutrition_index,
        'weight_index': weight_index,
        'lifespan_score': lifespan_score
    }

    return structured_output

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.json:
        return jsonify({'status': 'error', 'message': 'No file provided'}), 400

    file_data = request.json['file']

    # Decode the base64 image data
    try:
        image_data = base64.b64decode(file_data.split(',')[1])
        image_path = 'uploaded_image.jpg'  # Temporary path for the uploaded image
        with open(image_path, 'wb') as img_file:
            img_file.write(image_data)
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Error saving image: ' + str(e)}), 400

    try:
        result = cnn_freshness_inference(image_path)
        os.remove(image_path)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred: ' + str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')  # Render the index page

if __name__ == "__main__":
    app.run(debug=True)
