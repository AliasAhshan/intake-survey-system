from flask import Blueprint, jsonify, request
from backend.models.survey import SurveyResponse
from backend import db

form_bp = Blueprint("form", __name__)

@form_bp.route("/api/form", methods=["GET"])
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

@form_bp.route("/api/submit", methods=["POST"])
def submit_form():
    data = request.json
    response = SurveyResponse(answers=data)
    db.session.add(response)
    db.session.commit()
    return jsonify({"message": "Submission successful!"}), 200
