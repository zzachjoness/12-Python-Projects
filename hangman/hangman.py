import words
import random
words = words.words
random_word = random.choice(words)
print(len(words))
print(f"your hangman word is {len(random_word)} characters long, start with your first guess")
print(random_word)
print("trying again")