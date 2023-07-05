class Player:
    def __init__(self, word="", range_of_words=None):
        self.word = word
        self.range_of_words = range_of_words if range_of_words else []

    def __repr__(self):
        return f"Player(word='{self.word}', range_of_words={self.range_of_words})"

    def get_word(self):
        return self.word.title()

    def check_words(self, checked_word):
        checked_word = checked_word.lower().strip()
        return checked_word in self.range_of_words

    def count_subwords(self):
        return len(self.range_of_words)

    def add_words(self, added_word):
        self.range_of_words.append(added_word)
