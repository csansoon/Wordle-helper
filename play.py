from hashlib import new
from colors import *
import json
from random import randint
from solver import WordleSolver

with open('data/words.json') as words_file:
    words = json.load(words_file)

blank = '_'
separator = ''
rounds = 6

def neutral(text):
    return f'{gray_bg}{gray_fg}{text}{reset}'
def red(text):
    return f'{red_bg}{red_fg}{text}{reset}'
def yellow(text):
    return f'{yellow_bg}{yellow_fg}{text}{reset}'
def green(text):
    return f'{green_bg}{green_fg}{text}{reset}'


def keyboard(fixed, wrong_position, incorrect):
    keys = ''
    for i in range(ord('A'), ord('Z') + 1):
        letter = chr(i)
        if letter in incorrect:
            keys = keys + red(letter) + separator
        elif letter in fixed:
            keys = keys + green(letter) + separator
        else:
            hint_found = False
            for hints in wrong_position:
                if letter in hints:
                    keys = keys + yellow(letter) + separator
                    hint_found = True
                    break
            if not hint_found:
                keys = keys + neutral(letter) + separator
    return keys


def human_input(fixed, wrong_position, incorrect):
    return input(f'\r{neutral(blank)}{separator}{neutral(blank)}{separator}{neutral(blank)}{separator}{neutral(blank)}{separator}{neutral(blank)}↩️    {keyboard(fixed, wrong_position, incorrect)}\r').upper()


def solver_input(fixed, wrong_position, incorrect):
    return solver.find_best_word(fixed = fixed, wrong_position = wrong_position, incorrect = incorrect)


def ask_for_input(fixed, wrong_position, incorrect):
    # return human_input(fixed, wrong_position, incorrect)
    return solver_input(fixed, wrong_position, incorrect)


def new_round(print_console = True):
    fixed = ['','','','','']
    wrong_position = [[],[],[],[],[]]
    incorrect = []

    wordle = words[randint(0, len(words))].upper()
    for round in range(rounds):
        guess = ask_for_input(fixed, wrong_position, incorrect)

        if len(guess) != 5:
            if print_console: print(f'{bad}The word must be 5 characters long.{reset}')
            continue

        if guess.lower() not in words:
            if print_console: print(f'{bad}That word is not in the words list.{reset}')
            continue

        score = 0
        for i in range(5):
            letter = guess[i]
            if wordle[i] == letter:
                if print_console: print(f'{green(letter)}{separator}', end = '')
                fixed[i] = letter
                score = score + 1
            elif letter in wordle:
                if print_console: print(f'{yellow(letter)}{separator}', end = '')
                wrong_position[i].append(letter)
            else:
                incorrect.append(letter)
                if print_console: print(f'{neutral(letter)}{separator}', end = '')

        if print_console: print()
        if score == 5:
            return True
    return False
                


if __name__ == '__main__':
    solver = WordleSolver()
    new_round()