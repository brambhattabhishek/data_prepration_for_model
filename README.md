# **Smart Quality Test System using Computer Vision**

This project is part of a competition aimed at creating a smart quality test system for India's biggest e-commerce company. The system utilizes camera vision technology to assess the quality and quantity of shipments, focusing on the detection of fresh produce and packaging items using object detection, freshness classification, and text recognition.

## **Table of Contents**

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
  - [Backend (Flask)](#backend-flask)
  - [Frontend (React)](#frontend-react)
- [Model Details](#model-details)
  - [Object Detection and Counting using YOLOv8](#object-detection-and-counting-using-yolov8)
  - [OCR for Text Extraction](#ocr-for-text-extraction)
- [Usage](#usage)
- [Results and Demo](#results-and-demo)
- [Future Work](#future-work)
- [Contributors](#contributors)

## **Project Overview**

This application automates quality inspection for an e-commerce company's shipments using computer vision technology. It focuses on:

1. **Object Detection and Counting** for fruits and vegetables.
2. **Freshness Classification** based on appearance.
3. **OCR-based Text Extraction** from product packaging.

The system can detect, classify, and count fruits/vegetables using the YOLOv8 object detection model and extract text details (like name, brand, price, etc.) from packaging materials using Optical Character Recognition (OCR).

## **Architecture**

- **Frontend:** React app for UI that interacts with the camera and displays real-time results.
- **Backend:** Flask server that processes images using trained models for object detection, counting, freshness detection, and OCR.
- **Object Detection and Counting (YOLOv8):** Model trained using Roboflow for object detection, counting items, and freshness classification.
- **OCR (Tesseract):** For extracting details from packaging text.

## **Technologies Used**

- **Frontend:**
  - React.js
  - Tailwind CSS
  - Axios (for API communication)

- **Backend:**
  - Flask
  - Tesseract OCR
  - YOLOv8 for object detection, counting, and freshness classification
  - TensorFlow/Keras for CNN-based tasks
  
- **Models:**
  - YOLOv8 (Trained on Roboflow dataset for object detection, counting, and freshness classification)
  - Tesseract OCR for text extraction

## **Installation and Setup**

### Backend (Flask)

1. **Clone the repository:**
    ```bash
    git clone https://github.com/brambhattabhishek/smart-quality-system.git
    cd smart-quality-system/backend
    ```

2. **Set up the Python environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask server:**
    ```bash
    flask run
    ```

This will start the Flask server at `http://127.0.0.1:5000`.

### Frontend (React)

1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```

2. **Install the required dependencies:**
    ```bash
    npm install
    ```

3. **Start the React app:**
    ```bash
    npm start
    ```

This will start the frontend at `http://localhost:3000`.

## **Model Details**

### **Object Detection and Counting using YOLOv8**

- **Model:** YOLOv8 (You Only Look Once) is a state-of-the-art object detection model that was trained on a custom dataset using **Roboflow**. It detects and classifies objects in images (such as fruits and vegetables) and can also count the number of items detected in each frame.

- **Training:** The model was trained on Roboflow with annotated datasets, focusing on detecting the type of item (e.g., apples, oranges, etc.), classifying their freshness (e.g., fresh, overripe), and counting the total number of items.

- **Usage:** In the application, this model is used to:
  - **Detect:** Identify the items in each shipment.
  - **Classify:** Determine the freshness of the produce (fresh or not fresh).
  - **Count:** Calculate the total number of items in the shipment, useful for quantity verification.

### **OCR for Text Extraction**

- **OCR Model:** The system uses **Tesseract OCR** to extract text from product packaging. It can read product names, prices, and other details, which are useful for verifying packaging labels and ensuring the correct product is being shipped.

## **Usage**

Once the app is running, users can upload images or use the camera to scan shipments. The backend processes these images to:

1. **Detect, classify, and count objects** using YOLOv8.
2. **Extract text** from the packaging using Tesseract OCR.

## **Results and Demo**

The results of the detection, counting, and freshness classification will be displayed in the React frontend in real time, along with the extracted text.

## **Future Work**

- Improve the accuracy of the freshness classification model.
- Add support for multi-lingual text extraction in OCR.
- Extend object detection to additional product categories.

## **Contributors**

- Abhishek Brahmbhatt (Frontend & Backend Developer)(IIITL)--> team leader

- Aman hayat --> data science (IIITL)
 
- Kunal --> cse (NSUT)
- Manyank verma --> cse (RIT)
