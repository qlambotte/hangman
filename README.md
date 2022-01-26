# Hangman

## Description

This repository contains an implementation of the game Hangman.

Contributor: Quentin Lambotte

## Requirements

The code needs python3 to run.

## Instruction

You have four possibilities in order to run a game.

1. *With default configuration.* In this case, you will have to guess a word picked from the default list with five lives.
```bash
python3 main.py
```

2. *With a number of lives of your choice*. In this case, you will have to guess a word picked from the default list with the number of lives you chose.
```bash
python3 main.py num_lives
```

3. *With a list of words of your choice*. In this case, you will have to guess a word picked from your list with five lives. In the following command, ` path_to_file` is a path to a text file containing your words. It is assumed that there is *one word* per line.
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
