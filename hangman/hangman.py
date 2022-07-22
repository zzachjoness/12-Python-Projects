import random
import string
from words import words

# alternative import
# import words
# words = words.words
def pick_word():
  word = random.choice(words)
  print(f"your hangman word is {len(word)} characters long, start with your first guess")
  print(word)
  return word

def hangman():

  word = pick_word()
  word_letters = set(word.upper())
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  user_word = set()
  
  while len(word_letters) > 0:
    print('used_letters: ',' '.join(used_letters))
    print('word letters:',' '.join(word_letters))
    user_letter = input('Guess a letter: ').upper()
    user_word = [for letter in word:
      if user_letter in word_letters:
        return letter.upper()
      else:
        return '-']

    if user_letter in alphabet and user_letter not in used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        print('good guess')
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print('you already used that character, try again dope')
    else:
      print("invalid character, try again asshole")

hangman()