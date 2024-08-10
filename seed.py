from app import db
from app.models import QuizQuestion

question1 = QuizQuestion(question="What is the correct file extension for Python files?", option1=".py", option2=".pyt", option3=".pt", option4=".p", correct_answer=".py")
question2 = QuizQuestion(question="How do you create a variable with the floating number 2.8?", option1="x = float(2.8)", option2="x = 2.8f", option3="x = 2.8", option4="float x = 2.8", correct_answer="x = float(2.8)")
question3 = QuizQuestion(question="What is the output of `print(2 ** 3)`?", option1="5", option2="8", option3="6", option4="7", correct_answer="8")

db.session.add(question1)
db.session.add(question2)
db.session.add(question3)
db.session.commit()
