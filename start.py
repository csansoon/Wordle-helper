import eel
from wordle import *

eel.init('web')

wordle = None

@eel.expose
def new_game():
    global wordle
    wordle = Wordle() 

@eel.expose
def guess(word):
    global wordle
    word = str.lower(word)
    try:
        wordle.guess(word)
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
def get_random_name():
    eel.prompt_alerts('Random name')

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))

@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')

eel.start('index.html')