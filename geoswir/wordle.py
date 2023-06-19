from letter_state import Letter_state

class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 6

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass

    def attempt(self, word:str):
        word = word.upper()
        self.attempts.append(word)
    def guess(self, word:str):
        word= word.upper()
        result =[]
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = Letter_state(word[i])
            letter.in_the_word = character in self.secret
            letter.in_the_position = character == self.secret[i]
            result.append(letter)
        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
    @property
    def can_atttempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
