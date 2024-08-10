from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import QuizQuestion

@app.route('/')
def index():
    questions = QuizQuestion.query.all()
    return render_template('index.html', questions=questions)

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz(id):
    question = QuizQuestion.query.get_or_404(id)
    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option == question.correct_answer:
            flash('Correct!', 'success')
        else:
            flash('Incorrect. The correct answer was: {}'.format(question.correct_answer), 'danger')
        
        next_question = QuizQuestion.query.filter(QuizQuestion.id > id).first()
        if next_question:
            return redirect(url_for('quiz', id=next_question.id))
        else:
            flash('Quiz Completed!', 'info')
            return redirect(url_for('index'))

    return render_template('quiz.html', question=question)

@app.route('/add', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question_text = request.form['question']
        option1 = request.form['option1']
        option2 = request.form['option2']
        option3 = request.form['option3']
        option4 = request.form['option4']
        correct_answer = request.form['correct_answer']

        new_question = QuizQuestion(
            question=question_text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_answer=correct_answer
        )

        db.session.add(new_question)
        db.session.commit()

        flash('Question added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_question.html')

