import random

import requests as requests

from classes import Question


def get_questions():
    url = "https://www.jsonkeeper.com/b/HN8M"
    results = requests.get(url).json()
    questions = []
    for result in results:
        questions.append(Question(
            question_text=result["q"],
            difficulty=result["d"],
            right_answer=result["a"]
        ))

    return questions

def statistics(questions):
    print("Вот и все!")
    print(f"Отвечено {len([i for i in questions if i.is_right_answer])} вопроса из {len(questions)}")
    print(f"Набранно {sum([i.get_points() for i in questions if i.is_right_answer])} баллов")


def user():
    questions = get_questions()
    random.shuffle(questions)
    print("Игра начинается!\n")
    for i in questions:
        print(i.build_question())
        user_answer = input()
        if i.is_correct(user_answer):
            print(i.build_positive_feedback())
        else:
            print(i.build_negative_feedback())
    statistics(questions)
