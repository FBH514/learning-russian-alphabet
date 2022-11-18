import re

from alphabet import CyrillicAlphabet, LatinAlphabet

cyrillic = CyrillicAlphabet()
latin = LatinAlphabet()

def main() -> None:
    print("Welcome to the quiz 'Guess the Cyrillic letter'!")
    while True:
        random_index = cyrillic.random_index()
        random_letter = cyrillic.random_letter(random_index)
        user_input(random_letter, random_index)
        remove_letter(random_index)
        if len(cyrillic.letters) == 0:
            if again():
                main()
            else:
                break


def user_input(random_letter: str, random_index: int) -> None:
    if random_letter is None:
        return
    while True:
        user_input = input(f'Enter the letter {random_letter}: ').lower()
        if latin.letters[random_index].lower() == user_input:
            print('Correct!')
        else:
            print('Incorrect!')
        print()
        break

def again():
    while True:
        user_input = input('Play again? (y/n): ').lower()
        if re.match(r'^(y|yes|ya|yeah)$', user_input):
            return True
        elif re.match(r'^(n|no|nope)$', user_input):
            return False
        else:
            print('Incorrect input!')

def remove_letter(index) -> None:
    cyrillic.remove_letter(index)
    latin.remove_letter(index)


if __name__ == "__main__":
    main()
