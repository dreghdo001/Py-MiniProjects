from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a list of Question class objects for all questions
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Game mechanism
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

