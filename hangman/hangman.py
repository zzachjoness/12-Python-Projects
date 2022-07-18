import random
from words import words

# alternative import
# import words
# words = words.words

word = random.choice(words)
print(len(words))
print(f"your hangman word is {len(word)} characters long, start with your first guess")
print(word)
print("trying again")
guess = input("type something:")