from wordle import Wordle
from diction import check_word
def main():
    print("Cześć graczu geologu")
    wordle = Wordle("erozja")

    while wordle.can_atttempt:
        x = input("wpisz słowo:")
        if check_word(x) != True:
            print("Nie ma takiego wyrazu. Wpisz inne!")
            continue
        if len(x) != wordle.WORD_LENGTH:
            print(f"słowo musi zawierać {wordle.WORD_LENGTH} znaków")
            continue
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep = "\n")
    if wordle.is_solved:
        print("gratulacje, zgadłeś")
    else:
        print("PRZEGRANA :(")
if __name__ == '__main__':
    main()
