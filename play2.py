from wordle import *

wordle = Wordle()

hints = '⬜⬜⬜⬜⬜'
while (wordle.round < wordle.max_rounds):
    try:
        wordle.guess(input(f'{hints} ({wordle.round}/{wordle.max_rounds})\n'))
        hints = ''
        for value in wordle.last_guess.state:
            if value == 0: square = '⬜'
            elif value == 1: square = '🟨'
            elif value == 2: square = '🟩'
            else: square = '❓'
            hints = hints + square
    except InvalidGuess as message:
        print(message)
print(hints)
print(f'Word was {str.upper(wordle.solution)}')