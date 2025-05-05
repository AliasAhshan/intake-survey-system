import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
