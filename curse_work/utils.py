import random
import requests
from basic_word import BasicWord


def load_jason_doc(path):
    response = requests.get(path)
    data = response.json()
    return data


def load_random_word(path):
    all_words = load_jason_doc(path)
    random_word = random.choice(all_words)

    basic_word = BasicWord(
        word=random_word["word"],
        range_of_words=random_word["subwords"]
    )

    return basic_word
