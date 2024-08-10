import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quiz.db'  # SQLite database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
