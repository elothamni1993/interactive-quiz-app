from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import QuizQuestion, User

@app.route('/')
def index():
    return render_template('quiz.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    username = request.form.get('username')
    # Store username in session
    session['username'] = username
    # Redirect to results page
    return redirect(url_for('results'))

@app.route('/results')
def results():
    # Retrieve username from session
    username = session.get('username', 'Guest')
    return render_template('results.html', user=username)

