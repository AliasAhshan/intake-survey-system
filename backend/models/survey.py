from backend import db

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answers = db.Column(db.JSON)
