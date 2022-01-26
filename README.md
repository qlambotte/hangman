# Hangman

## Description

This repository contains an implementation of the game Hangman. This game consists in guessing a word letter by letter with a fixed number of allowed mistakes (with repetitions). The default number of liines is 5 and the default list from wich a word is chosen from is `['becode', 'learning', 'mathematics', 'sessions']`. These parameters can be changed - see Instructions below. This repository is organized as follows:
```
hangman
|
└───utils
|     └───game.py
└───data
|     └───data_good.txt
|     └───data_wrong.txt
└───main.py
```

The file `./utils/game.py` contains the core of the program. The textfiles in `./data/` contains words (one per line), the good one meets the requirements expaleined in the Instructions while the other does not.

Contributor: Quentin Lambotte

## Requirements

The code needs python3 to run.

## Instructions

You have four possibilities in order to run a game.

1. *With default configuration.* In this case, you will have to guess a word picked from the default list with five lives.
```bash
python3 main.py
```

2. *With a number of lives of your choice*. In this case, you will have to guess a word picked from the default list with the number of lives you chose.
```bash
python3 main.py num_lives
```

3. *With a list of words of your choice*. In this case, you will have to guess a word picked from your list with five lives. In the following command, ` path_to_file` is a path to a text file containing your words. It is assumed that there is *one word* per line and that the file contains the words becode, learning, mathematics and sessions.
```bash
python3 main.py path_to_file
```

4. *With a list of words and number of lives of your choice*.
In this case, you will have to guess a word picked from your list with the
number of lives you chose. In the following command, ` path_to_file` is a path
to a text file containing your words. It is assumed that there is *one word*
per line. It is also assumes that the number of lives is the *first* argument.
```bash
python3 main.py num_lives path_to_file
