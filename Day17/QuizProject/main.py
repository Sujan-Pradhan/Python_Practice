from question_models import Question
from data import questions
from quiz_ideas import QuizIdea


question_bank = []
for question in questions:
    # print (question)
    q_question = question["question"] 
    question_answer = question["correct_answer"]
    new_question = Question(q_question, question_answer)
    question_bank.append(new_question)


quiz = QuizIdea(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")