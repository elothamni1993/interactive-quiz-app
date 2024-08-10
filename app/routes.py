from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import QuizQuestion, User, QuizAnswer

@app.route('/')
def index():
    questions = QuizQuestion.query.all()
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    if not username:
        return redirect(url_for('index'))

    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

    for question_id in request.form:
        if question_id != 'username':
            selected_option = request.form.get(question_id)
            answer = QuizAnswer(question_id=question_id, user_id=user.id, selected_option=selected_option)
            db.session.add(answer)
    
    db.session.commit()
    return redirect(url_for('results', username=username))

@app.route('/results')
def results():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first_or_404()
    answers = QuizAnswer.query.filter_by(user_id=user.id).all()
    return render_template('results.html', user=user, answers=answers)
