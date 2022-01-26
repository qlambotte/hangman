import re
from random import choice


class InvalidWordList(Exception):
    """
    Exception raised when the list of possible words do not contain
    "becode", "learning", "mathematics", "sessions".
    """

    pass


class Hangman:
    """
    Implementation of the game Hangman.

    Pramaeters
    ----------
    possible_words : list[str]
        This is a list of words. This list must contain the words becode,
        learning, mathematics and sessions. The default value is
        ["becode", "learning", "mathematics", "sessions"].
    lives: int
        This represents the number of lives during the game. The default value
        is 5.

    Attributes
    ----------
    possible_words : list[str]
    lives : int
    word_to_find : str
    correctly_guessed_letters : list[str]
    wrongly_guessed_letters : Set[str]
    turn_count : int
    error_count : int
    """

    possible_words = ["becode", "learning", "mathematics", "sessions"]

    def __init__(
        self, possible_words: list[str] = possible_words, lives: int = 5
    ) -> None:
        """
        Constructor of the class.

        Arguments
        ---------
        possible_words : List[str]
        lives : int

        Exception
        ---------
        Raises InvalidWordList if possible_words does not contain one of becode,
        learning, mathematics, sessions.
        """
        if not all(
            s in possible_words
            for s in ["becode", "learning", "mathematics", "sessions"]
        ):
            raise InvalidWordList(
                "The list :possible_words: should contain becode, learning, mathematics and sessions."
            )
        self.word_to_find = choice(possible_words).upper()
        self.lives = lives
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = set()
        self.turn_count = 0
        self.error_count = 0

    def game_over(self) -> None:
        """
        This method implements how the game ends when loosing.
        """
        assert self.lives == 0
        print(f"Game over... You had to guess {self.word_to_find}")

    def well_played(self) -> None:
        """
        This method implements how the game ends when winning.
        """
        turns = self.turn_count
        errors = self.error_count
        assert turns > 0 and not (turns == 1 and errors > 0)
        if turns == 1:
            print(
                f"You found the word: {self.word_to_find} in \
{turns} turn with no erros!"
            )
        else:
            print(
                f"You found the word {self.word_to_find} in \
{turns} turns with {errors} errors!"
            )

    def play(self) -> None:
        """
        This method implements the differents spets in a turn of the game.
        """
        letter = input("Please enter a letter: ")
        # check if letter is indeed just a letter
        r = re.compile(r"^[a-zA-Z]$")
        while not re.match(r, letter):
            letter = input(
                f"You did not enter a letter \
(you entered {letter}). Please enter a letter: "
            )
        letter = letter.capitalize()
        if letter in self.word_to_find:
            ind = [n for n, s in enumerate(self.word_to_find) if s == letter]
            for i in ind:
                self.correctly_guessed_letters[i] = letter
        else:
            self.wrongly_guessed_letters.add(letter)
            self.lives -= 1

    def start_game(self) -> None:
        """
        This method starts the game and ultimately ends it.
        """
        word_split = list(self.word_to_find)
        while self.lives > 0:
            self.play()
            self.turn_count += 1
            if word_split == self.correctly_guessed_letters:
                self.well_played()
                break
            guess = " ".join(self.correctly_guessed_letters)
            errors = ", ".join(self.wrongly_guessed_letters)
            self.error_count = len(self.wrongly_guessed_letters)
            # this long if-else block is there to take car of the grammar
            # in the messages depending on the number of counts and errors.
            if self.error_count == 0:
                if self.turn_count == 1:
                    print(
                        f"So far, you guessed {guess} with no error \
in {self.turn_count} turn."
                    )
                else:
                    print(
                        f"So far, you guessed {guess} with no error \
in {self.turn_count} turns."
                    )
            else:
                if self.turn_count == 1:
                    print(
                        f"So far, you guessed {guess} with {self.error_count}\
 error ({errors}) in {self.turn_count} turn."
                    )
                elif self.error_count == 1:
                    print(
                        f"So far, you guessed {guess} with {self.error_count}\
 error ({errors}) in {self.turn_count} turns."
                    )
                else:
                    print(
                        f"So far, you guessed {guess} with {self.error_count}\
 errors ({errors}) in {self.turn_count} turns."
                    )
            if self.lives > 1:
                print(f"You have {self.lives} lives remaining.\n")
            else:
                print(f"You have {self.lives} life remaining.\n")
        if self.lives == 0:
            self.game_over()
