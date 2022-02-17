class EmptyWordlist(Exception):
    pass

class InvalidGuess(Exception):
    pass

# Each state of the Guess can be 0 (wrong), 1 (right letter but wrong position) or 2 (correct)
class Guess:

    def __init__(self, word, solution):
        # Initialize
        self.word = str.lower(word)
        self.state = []
        for i in range(len(solution)):
            self.state.append(0)

        if len(word) != len(solution):
            raise InvalidGuess(f'Word ({word}) length is different than solution ({len(solution)})')

        # Find state from word and solution
        solution_tmp = solution
        for i in range(len(solution)):
            if word[i] == solution[i]:
                solution_tmp = Guess.__remove_letter(solution_tmp, word[i])
                self.state[i] = 2
        for i in range(len(solution)):
            if self.state[i] == 0 and word[i] in solution_tmp:
                solution_tmp = Guess.__remove_letter(solution_tmp, word[i])
                self.state[i] = 1

    def __remove_letter(word, letter):
        length = len(word)
        for i in range(length):
            if(word[i] == letter):
                return word[0:i] + word[i + 1:length]
        return word
        

class Wordle:

    def __init__(self, word=None, max_rounds=6, wordlist=None):
        self.solution = word
        self.round = 0
        self.max_rounds = max_rounds
        self.__init_wordlist(wordlist)
        self.guesses = []
        self.last_guess = None
    
    def __init_wordlist(self, wordlist):
        if wordlist is None and self.solution is None:
            import json
            import random
            with open('data/answers.json') as words_file:
                self.solution = str.lower(random.choice(json.load(words_file))['word'])

        if wordlist is None:
            import json
            with open('data/words.json') as words_file:
                self.wordlist = json.load(words_file)
        else:
            self.wordlist = wordlist
        
        if self.solution is None:
            self.solution = str.lower(random.choice(wordlist))
        
        if not self.wordlist: raise EmptyWordlist()
        
        for word in self.wordlist:
            if len(word) != len(self.solution):
                self.wordlist.remove(word)
        
        if not self.wordlist:
            raise EmptyWordlist("There are no words of the same size of the solution in the wordlist.")

        
    def guess(self, word):
        if len(word) != len(self.solution):
            raise InvalidGuess("Guess length is different than the length of the solution.")
        if word not in self.wordlist:
            raise InvalidGuess("Word not in list.")
        if self.round >= self.max_rounds:
            raise InvalidGuess("Game is over.")
        word = str.lower(word)
        current_guess = Guess(word, self.solution)
        self.last_guess = current_guess
        self.guesses.append(current_guess)
        self.round = self.round + 1
        return self.guesses
        
    def get_wordlist(self):
        return self.wordlist