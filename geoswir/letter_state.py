class Letter_state:
    def __init__(self, character: str):
        self.character: str = character
        self.in_the_word: bool = False
        self.in_the_position: bool = False
    def __repr__(self):
        return f"[litera {self.character} w słowie: {self.in_the_word} \n   w pozycji: {self.in_the_position}]"