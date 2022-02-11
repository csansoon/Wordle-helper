
from numpy import empty


class EmptyWordlist(Exception):
    pass

class Wordle:

    def __init__(self, word=None, tries=6, wordlist=None):
        self.solution = word
        self.round = 0
        self.tries = tries
        self.__init_wordlist(wordlist)
    
    def __int_wordlist(self, wordlist):
        if wordlist is None:
            import json
            with open('data/words.json') as words_file:
                self.wordlist = json.load(words_file)
        else:
            self.wordlist = wordlist
        
        if not self.wordlist: raise EmptyWordlist()
        
        if self.solution is None:
            import random
            self.solution = str.lower(random.choice(self.wordlist))
        
        for word in self.worldlist:
            if len(word) != len(self.solution):
                self.wordlist.remove(word)
        

