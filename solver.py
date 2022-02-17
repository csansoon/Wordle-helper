from wordle import *
from operator import itemgetter

class WordleSolver:
    def __init__(self, wordlist, possible_words = None):
        self.wordlist = wordlist
        if possible_words is None:
            self.possible_words = wordlist
        else:
            self.possible_words = possible_words
    
    def update_possible_words(self, guess):
        self.possible_words = WordleSolver.discard(self.possible_words, guess)
        return self.possible_words
    
    def get_best_answers(self):
        wordlist_score = []
        len_possible_words = len(self.possible_words)
        for word in self.wordlist:
            score = 0
            for possible_solution in self.possible_words:
                score = score + len_possible_words - len(WordleSolver.discard(self.possible_words, Guess(word, possible_solution)))
            if score > 0:
                wordlist_score.append({
                    'word': word,
                    'score': score / len(self.possible_words)
                })
        return sorted(wordlist_score, key=itemgetter('score'), reverse=True)

    
    def discard(wordlist, guess):
        possible_words = []
        for possible_answer in wordlist:
            if possible_answer == guess.word: pass
            if Guess(guess.word, possible_answer).state == guess.state:
                possible_words.append(possible_answer)
        return possible_words