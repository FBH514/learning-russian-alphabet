import random
from typing import Optional


class Alphabet:

    def __init__(self) -> None:
        self.letters: list = []

    def cyrillic_alphabet(self) -> None:
        self.letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    def latin_alphabet(self) -> None:
        self.letters = ['A', 'B', 'V', 'G', 'D', 'E', 'Jo', 'Zh', 'Z', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'Kh', 'C', 'Ch', 'Sh', 'Shh', '\"', 'Y', '\'', 'Eh', 'Ju', 'Ja']

    def print_letters(self) -> None:
        print('Letters: ', end='')
        for letter in self.letters:
            print(letter, end=' ')
        print()

    def check_letter(self, letter) -> bool:
        left = 0
        right = len(self.letters) - 1
        while left <= right:
            middle = (left + right) // 2
            if letter == self.letters[middle]:
                return True
            elif letter < self.letters[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def random_index(self) -> Optional[int]:
        if len(self.letters) > 0:
            return random.randint(0, len(self.letters) - 1)
        return None

    def random_letter(self, index) -> Optional[str]:
        if index is not None:
            return self.letters[index]
        return None

    def remove_letter(self, index) -> None:
        if index is not None:
            self.letters.pop(index)

class CyrillicAlphabet(Alphabet):

    def __init__(self) -> None:
        super().__init__()
        self.cyrillic_alphabet()

    def __repr__(self) -> str:
        return f"Cyrillic Alphabet {' '.join(self.letters)}"

class LatinAlphabet(Alphabet):

    def __init__(self) -> None:
        super().__init__()
        self.latin_alphabet()

    def __repr__(self) -> str:
        return f"Latin Alphabet {' '.join(self.letters)}"