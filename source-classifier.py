import json

with open('data/source.txt', 'r') as file:
    lines = file.readlines()
    lines.pop(0)

answers = []
words = []

for line in lines:
    data = line.split('\t')
    word = data[2].replace('\n','').lower()
    date = data[0]
    id = data[1]

    words.append(word)

    if int(id) < 2315:
        wordle = {
            'id': id,
            'date': date,
            'word': word
        }
        answers.append(wordle)

words.sort()

with open('data/words.json', 'w') as words_file:
    json.dump(words, words_file)

with open('data/answers.json', 'w') as answers_file:
    json.dump(answers, answers_file)

print(f'✅ Loaded a total of {len(words)} words and {len(answers)} answers.')