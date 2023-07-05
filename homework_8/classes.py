from pathlib import Path


class Question:
    question_text: str = None
    difficulty: str = None
    right_answer: str = None

    is_asked: bool = False
    answer: str = None
    __points: int = None
    is_right_answer: bool = False

    def __init__(self, question_text: str, difficulty: str, right_answer: str):
        self.question_text: str = question_text
        self.difficulty: str = difficulty
        self.right_answer: str = right_answer
        self.__points = int(self.difficulty) * 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.__points


    def is_correct(self, user_answer: str):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        self.answer = user_answer
        return self.answer.lower() == self.answer.strip().lower()

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        self.is_asked = True
        return f"Вопрос: {self.question_text}\nСложность {self.difficulty}/5"


    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        self.is_right_answer = True
        return f"Ответ верный, получено {self.get_points()} баллов"

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f"Ответ неверный, верный ответ {self.right_answer}"


ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)