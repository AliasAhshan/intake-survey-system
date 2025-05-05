# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
