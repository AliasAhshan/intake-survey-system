# backend/app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Load .env
env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

# Use the value from .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Example model to store form answers
class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answers = db.Column(db.JSON)

@app.route("/api/form", methods=["GET"])
def get_form():
    return jsonify({
        "title": "Sample Intake Form",
        "questions": [
            {
                "id": "has_kids",
                "text": "Do you have kids?",
                "type": "radio",
                "options": ["Yes", "No"]
            }
        ]
    })

@app.route("/api/submit", methods=["POST"])
def submit_form():
    data = request.json
    print("Received submission:", data)
    return jsonify({"message": "Submission successful!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
