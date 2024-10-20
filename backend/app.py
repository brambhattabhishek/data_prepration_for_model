from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        data = request.get_json()  # Get the JSON data
        file = data.get('file')  # Extract the base64 file string
        
        if not file:
            return jsonify({'message': 'No file provided.'}), 400

        # Process the file (e.g., save it, run OCR, etc.)
        # For now, let's assume we're just returning a dummy response
        response = {
            'message': 'File uploaded successfully!',
            'status': 'success',
            'ocr_results': {
                'name': 'Sample Fruit'
            },
            'freshness_index': {'value': 95},
            'ripeness_stage_index': {'value': 70},
            'size_index': {'value': 80},
            'color_index': {'value': 90},
            'nutrition_index': {'value': 85},
            'weight_index': {'value': 100},
            'lifespan_score': {'value': 75},
        }

        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
