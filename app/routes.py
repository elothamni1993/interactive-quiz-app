from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Quiz, User

@app.route('/')
def index():
    return render_template('quiz.html')

@app.route('/results')
def results():
    # Handle result calculation and display
    return render_template('results.html')

