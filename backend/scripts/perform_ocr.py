import pytesseract
from pytesseract import Output
import cv2

def perform_ocr(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to RGB (Tesseract expects RGB images)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Perform OCR on the image
    ocr_data = pytesseract.image_to_data(img_rgb, output_type=Output.DICT)

    # Initialize the extracted_info dictionary with default values
    extracted_info = {
        'product_name': None,
        'brand': None,
        'price': None,
        'expiration_date': None,
        'size': None,
        'weight': None,
        'ingredients': None
    }

    # Loop through the OCR results and populate the extracted_info dictionary
    for i in range(len(ocr_data['text'])):
        text = ocr_data['text'][i].strip()
        if text:
            # Logic to classify extracted text into relevant fields
            if 'price' in text.lower():
                extracted_info['price'] = text
            elif 'exp' in text.lower() or 'expiration' in text.lower():
                extracted_info['expiration_date'] = text
            elif 'size' in text.lower():
                extracted_info['size'] = text
            elif 'weight' in text.lower():
                extracted_info['weight'] = text
            elif 'ingredient' in text.lower() or 'ingredients' in text.lower():
                extracted_info['ingredients'] = text
            elif not extracted_info['brand'] and text.isalpha():  # Assuming brand names are alphabetic
                extracted_info['brand'] = text
            elif not extracted_info['product_name']:  # Assuming the first text is the product name
                extracted_info['product_name'] = text

    # Clean up any fields that may still be None
    for key in extracted_info:
        if extracted_info[key] is None:
            extracted_info[key] = 'Not Found'

    # Return structured output
    structured_output = {
        'status': 'success',
        'extracted_info': extracted_info
    }

    return structured_output

# Example usage
if __name__ == "__main__":
    image_path = 'path/to/your/image.jpg'  # Replace with your image path
    ocr_result = perform_ocr(image_path)
    print(ocr_result)
