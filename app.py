from flask import Flask, redirect, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, personality_quiz
app = Flask(__name__)
app.config['SECRET_KEY'] = "doingstuff"
debug = DebugToolbarExtension(app)

responses = []
count = 0


@app.route("/")
def survey_home():
    """Survey Home Page"""
    instructions = satisfaction_survey.instructions
    return render_template('survey.html', title=satisfaction_survey.title, instructions=instructions, count=count)


@app.route('/questions/<count>')
def question_pages(count):
    """Question pages"""
    question = satisfaction_survey.questions[int(count)]
    return render_template('questions.html', question=question.question, answers=question.choices, count=count)


@app.route('/answer', methods=['POST'])
def answer_question():
    """Take answer, append to responses, and up count"""
    answer = request.form['answer']
    responses.append(answer)
    return redirect('/')
