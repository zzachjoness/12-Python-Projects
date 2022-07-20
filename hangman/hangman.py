import random
import string
from words import words

# alternative import
# import words
# words = words.words

word = random.choice(words)
print(f"your hangman word is {len(word)} characters long, start with your first guess")
print(word)

def hangman():
  word_letters = set(word.upper())
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  print('word letters: ', word_letters)
  while len(word_letters) > 0:
    print('You have used these letters: ',' '.join(used_letters))
    #List Comprehension
    word_list = [letter for letter in word_letters & used_letters or '-']
    print('wordlist: ',' '.join(word_list))
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        print('good guess')
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print('you already used that character, try again dope')
    else:
      print("invalid character, try again asshole")

hangman()