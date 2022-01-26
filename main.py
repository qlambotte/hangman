import utils.game as game
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        hang = game.Hangman()
        hang.start_game()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg.isdigit():
            hang = game.Hangman(lives=int(arg))
            hang.start_game()
        else:
            with open(arg, "r") as file:
                possible_words = file.read().split("\n")
            hang = game.Hangman(possible_words=possible_words)
            hang.start_game()
    else:
        with open(sys.argv[2], "r") as file:
            possible_words = file.read().split("\n")
        hang = game.Hangman(
            lives=int(sys.argv[1]), possible_words=possible_words
        )
        hang.start_game()
