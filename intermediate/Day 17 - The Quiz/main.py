import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in data.question_data:
    question_bank.append(Question(question["difficulty"], question["category"], question["question"], question["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}.")