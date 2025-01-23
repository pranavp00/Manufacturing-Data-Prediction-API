Manufacturing Data Prediction API

Overview

This project is a Flask-based API for uploading, training, and predicting manufacturing data. It provides endpoints to:

Upload a CSV file containing manufacturing data.

Train a Random Forest model using the uploaded dataset.

Predict downtime using input parameters.

The backend ensures validation of uploaded files and provides performance metrics like accuracy, F1-score, and Cohen's Kappa for model evaluation. A frontend interface built with HTML, CSS, and JavaScript is included for uploading files and interacting with the API.

Features

Upload Endpoint: Accepts CSV files for data upload.

Train Endpoint: Trains a Random Forest model using uploaded data and returns performance metrics.

Predict Endpoint: Accepts JSON input to predict manufacturing downtime.

Frontend Interface: Simple web interface for file uploads and prediction requests.

Technical Stack

Backend: Flask, scikit-learn, pandas

Frontend: HTML, CSS, JavaScript

Environment Management: Python (venv), pip

Prerequisites

Python 3.8+

pip (Python package manager)

Postman or cURL for testing API endpoints (optional)

Setup Instructions

Step 1: Clone the Repository

git clone <repository_url>
cd <repository_folder>

Step 2: Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run the Flask Application

python app.py

The API will be accessible at http://127.0.0.1:5000/.

API Endpoints

1. Upload Endpoint

URL: POST /upload

Description: Accepts a CSV file containing manufacturing data with the following columns: Air temperature, Rotational speed, Tool wear, and Target.

Example Request:

curl -X POST -F "file=@data.csv" http://127.0.0.1:5000/upload

Example Response:

{
    "message": "File uploaded successfully!",
    "data_preview": [
        {"Air temperature": 25, "Rotational speed": 1500, "Tool wear": 200, "Target": "Yes"},
        {"Air temperature": 30, "Rotational speed": 1400, "Tool wear": 250, "Target": "No"}
    ]
}

2. Train Endpoint

URL: POST /train

Description: Trains the model using the uploaded data and returns metrics.

Example Request:

curl -X POST http://127.0.0.1:5000/train

Example Response:

{
    "message": "Model trained successfully!",
    "metrics": {
        "accuracy_mean": 0.92,
        "f1_score_mean": 0.89,
        "kappa_mean": 0.88
    }
}

3. Predict Endpoint

URL: POST /predict

Description: Accepts JSON input to predict downtime.

Input Format:

{
    "Air temperature": 30,
    "Rotational speed": 1400,
    "Tool wear": 250
}

Example Request:

curl -X POST -H "Content-Type: application/json" -d '{"Air temperature": 30, "Rotational speed": 1400, "Tool wear": 250}' http://127.0.0.1:5000/predict

Example Response:

{
    "Downtime": "Yes",
    "Confidence": 0.85
}

Example Frontend Interaction

Open the index.html file in your browser.

Use the interface to:

Upload a CSV file.

Train the model.

Input parameters for predictions.

Testing the API

Use Postman or cURL to send requests to the endpoints.

Validate responses and check performance metrics after training.


Future Enhancements

Add authentication for secure API access.

Improve model explainability with feature importance visualization.

Extend support for additional machine learning algorithms.

License

This project is licensed under the MIT License.
