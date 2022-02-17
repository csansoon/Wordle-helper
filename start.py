import eel
from wordle import *
from solver import WordleSolver

eel.init('web')

wordle = None
solver = None

@eel.expose
def new_game():
    global wordle
    global solver
    wordle = Wordle() 
    solver = WordleSolver(wordle.get_wordlist())

@eel.expose
def guess(word):
    global wordle
    word = str.lower(word)
    try:
        wordle.guess(word)
        solver.update_possible_words(wordle.last_guess)
        return wordle.last_guess.state;
    except InvalidGuess as errormsg:
        eel.show_error(str(errormsg));
        return False

@eel.expose
def get_answer():
    global wordle
    if wordle:
        return str.upper(wordle.solution)
    return None;

@eel.expose
def update_possible_words():
    global solver
    eel.set_answers(solver.possible_words)

@eel.expose
def update_best_guesses():
    global solver
    wordlist_score = solver.get_best_answers()
    eel.set_guesses(wordlist_score)


eel.start('index.html')