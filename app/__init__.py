from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class
db = SQLAlchemy(app)

from app import routes, models
