class BasicWord:
    def __init__(self, word="", range_of_words=None):
        self.word = word
        self.range_of_words = range_of_words if range_of_words else []

    def __repr__(self):
        return f"BasicWord(word='{self.word}', range_of_words={self.range_of_words})"

    def get_word(self):
        return f"{self.word.upper()}"

    def check_words(self, checked_word):
        checked_word = checked_word.lower().strip()
        return checked_word in self.range_of_words

    def count_subwords(self):
        return len(self.range_of_words)
