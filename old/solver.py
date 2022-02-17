import json

class WordleSolver:
    def analyse_words(self):
        self.words = []
        with open('data/words.json') as words_file:
            raw_words = json.load(words_file)

        appearances = [{},{},{},{},{}]
        for word in raw_words:
            for i in range(len(word)):
                letter = word[i]
                if letter not in appearances[i]:
                    appearances[i][letter] = 0
                appearances[i][letter] = appearances[i][letter] + 1
        for word in raw_words:
            score = 0
            for i in range(len(word)):
                letter = word[i]
                score = score + appearances[i][letter]
            self.words.append({
                'word': word.upper(),
                'score': score
            })


    def __init__(self):
        self.analyse_words()
        
    def find_best_word(self, fixed = ['','','','',''], wrong_position = [[],[],[],[],[]], incorrect = [], count = 1, show_scores = False):
        if len(fixed) != 5:
            raise ValueError('Invalid number of fixed characters.')
        if len(wrong_position) != 5:
            raise ValueError('Invalid number of wrong positioned letters.')
        
        bests = []
        for i in range(count):
            bests.append({
                'word': '',
                'score': 0
            })

        for wordle in self.words:
            word = wordle['word']
            score = wordle['score']
            valid = True

            for i in range(5):
                if fixed[i] != '' and ord(fixed[i].upper()) >= ord('A') and ord(fixed[i].upper()) <= ord('Z'): # If there is a fixed letter here
                    if fixed[i] != word[i]:
                        valid = False
                        break
                elif word[i] in incorrect or word[i] in wrong_position[i]:
                    valid = False
                    break
            for position in wrong_position:
                for letter in position:
                    if not letter in word:
                        valid = False
                        break
                    if not valid: break

            if valid:
                for i in range(count):
                    if score > bests[i]['score']:
                        for j in reversed(range(i + 1, count)):
                            bests[j] = bests[j - 1]
                        new_best = {'word': word, 'score': score}
                        bests[i] = new_best
                        break
                
        if show_scores:
            return bests

        if count == 1:
            return bests[0]['word']
        
        result = []
        for i in range(count):
            result.append(bests[i]['word'])
        return result
                
