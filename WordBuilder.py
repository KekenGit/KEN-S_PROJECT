# Imports itertools to generate different combinations
from itertools import permutations

# Accepts a word from the user
word = input("Enter a word: ")

# Creates a set to avoid duplicate words
possible_words = set()

# Loops through all possible arrangements of letters
for p in permutations(word):

    # Joins letters into a complete word
    new_word = ''.join(p)

    # Adds the word to the set
    possible_words.add(new_word)

# Displays all possible words
print("Possible words are:")

for w in possible_words:
    print(w)