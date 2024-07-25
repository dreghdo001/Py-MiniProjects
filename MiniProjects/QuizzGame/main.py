from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

import random
question_bank = []

for items in question_data:
    text = items['question']
    answer = items['correct_answer']
    Question = QuestionModel(text,answer)
    question_bank.append(Question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_print()