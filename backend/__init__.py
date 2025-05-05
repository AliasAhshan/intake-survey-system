from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)

    # Register Blueprints
    from backend.routes.form import form_bp
    app.register_blueprint(form_bp)

    return app
