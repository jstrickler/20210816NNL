from pprint import pprint

first_letters = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        letter = line[0]
        if letter in first_letters:
            first_letters[letter] += 1
        else:
            first_letters[letter] = 1

pprint(first_letters)
