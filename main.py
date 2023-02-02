import re
from alphabet import CyrillicAlphabet, LatinAlphabet

cyrillic = CyrillicAlphabet()
latin = LatinAlphabet()

score = {"marks": 0, "total": 0}

def main() -> None:
    """
    Main function
    :return: None
    """
    print("Welcome to 'Guess the Cyrillic letter'!")
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
    print(f'Your score is {score["marks"]} out of {score["total"]}')


def keep_score(mark: int = 1, total: int = 1) -> None:
    """
    Keeps score of the game
    :param mark: mark to add to the score
    :param total: total to add to the score
    :return: None
    """
    score["marks"] += mark
    score["total"] += total


def user_input(random_letter: str, random_index: int) -> None:
    """
    Asks user to guess the letter
    :param random_letter: random letter
    :param random_index: random index
    :return: None
    """
    if random_letter is None:
        return
    while True:
        user_input = input(f'Enter the letter {random_letter}: ').lower()
        if user_input.isspace() or user_input == '':
            continue
        elif latin.letters[random_index].lower() == user_input.lower():
            keep_score()
            print('Correct!\n')
        else:
            keep_score(0)
            print(f'Incorrect! Answer was {latin.letters[random_index]}\n')
        break


def again() -> bool:
    """
    Asks user if they want to play again
    :return: True if user wants to play again, False otherwise
    """
    while True:
        user_input = input('Play again? (y/n): ').lower()
        if re.match(r'^(y|yes|ya|yeah)$', user_input):
            return True
        elif re.match(r'^(n|no|nope)$', user_input):
            return False
        else:
            print('Incorrect input!')


def remove_letter(index: int) -> None:
    """
    Removes letter from the list
    :param index: index of the letter to remove
    :return: None
    """
    cyrillic.remove_letter(index)
    latin.remove_letter(index)


if __name__ == "__main__":
    main()
