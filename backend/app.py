from flask import Flask, request, jsonify
import os
import pandas as pd
from model import train_model, make_prediction
from utils import validate_csv, validate_json

app = Flask(__name__)

# Global variables to store uploaded data and the trained model
DATA_FILE = None
MODEL = None

UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "hello world"

@app.route("/upload", methods=["POST"])
def upload_file():
    global DATA_FILE
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith(".csv"):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        data = pd.read_csv(file_path)

        if not validate_csv(data):
            return jsonify({"error": "Invalid CSV file format."}), 400

        DATA_FILE = data
        return jsonify({"message": "File uploaded successfully!"}), 200
    else:
        return jsonify({"error": "Only CSV files are accepted."}), 400

@app.route("/train", methods=["POST"])
def train():
    global DATA_FILE, MODEL
    if DATA_FILE is None:
        return jsonify({"error": "No data uploaded."}), 400

    MODEL, metrics = train_model(DATA_FILE)
    return jsonify({
        "message": "Model trained successfully!",
        "metrics": {
            "accuracy_mean": metrics["accuracy_mean"],
            "f1_score_mean": metrics["f1_score_mean"],
            "kappa_mean": metrics["kappa_mean"]
        }
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    global MODEL
    if MODEL is None:
        return jsonify({"error": "Model not trained yet."}), 400

    input_data = request.get_json()
    if not validate_json(input_data):
        return jsonify({"error": "Invalid JSON input format."}), 400

    prediction, confidence = make_prediction(MODEL, input_data)
    return jsonify({"Downtime": prediction, "Confidence": confidence}), 200

if __name__ == "__main__":
    app.run(debug=True)
