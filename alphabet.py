import random
from typing import Optional


class Alphabet:

    def __init__(self) -> None:
        """
        Initializes the Alphabet object
        """
        self.letters: list = []

    def cyrillic_alphabet(self) -> None:
        """
        Cyrillic alphabet
        :return: list of cyrllic letters
        """
        self.letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    def latin_alphabet(self) -> None:
        """
        Latin alphabet
        :return: list of latin letters
        """
        self.letters = ['A', 'B', 'V', 'G', 'D', 'E', 'Jo', 'Zh', 'Z', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'Kh', 'C', 'Ch', 'Sh', 'Shh', '\"', 'Y', '\'', 'Eh', 'Ju', 'Ja']

    def random_index(self) -> Optional[int]:
        """
        Returns random index of the letter
        :return: random index
        """
        if len(self.letters) > 0:
            return random.randint(0, len(self.letters) - 1)
        return None

    def random_letter(self, index) -> Optional[str]:
        """
        Returns random letter
        :param index: index of the letter
        :return:
        """
        if index is not None:
            return self.letters[index]
        return None

    def remove_letter(self, index) -> None:
        """
        Removes letter from the list
        :param index: index of the letter to remove
        :return: None
        """
        if index is not None:
            self.letters.pop(index)

class CyrillicAlphabet(Alphabet):

    def __init__(self) -> None:
        """
        Initializes the CyrillicAlphabet object
        Inherits from Alphabet
        :return: None
        """
        super().__init__()
        self.cyrillic_alphabet()

    def __repr__(self) -> str:
        """
        Returns string representation of the object
        :return: string representation of the object
        """
        return f"Cyrillic Alphabet {' '.join(self.letters)}"

class LatinAlphabet(Alphabet):

    def __init__(self) -> None:
        """
        Initializes the LatinAlphabet object
        Inherits from Alphabet
        :return: None
        """
        super().__init__()
        self.latin_alphabet()

    def __repr__(self) -> str:
        """
        Returns string representation of the object
        :return: string representation of the object
        """
        return f"Latin Alphabet {' '.join(self.letters)}"
