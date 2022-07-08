import random

############################################################################################################
# Literal

def error():
  print("an error occured, this is awkward")

def win():
  print("you win, YAY!")

def lose():
  print("you lose, so sad!")

def label(choice):
  if choice == "r":
    return "rock"
  if choice == "p":
    return "paper"
  if choice == "s":
    return "scisors"


def game():
  user = input("choose 'r' for rock, 'p' for paper, 's' for scisors: ")
  computer = random.choice(['r','p','s'])
  print(f"you chose {label(user)}, the computer chose {label(computer)}...")
  if user == computer:
    print("It's a tie, try again")
    game()
  if user == 'r':
    if computer == 's':
      win()
    elif computer == 'p':
      lose()
  elif user == 'p':
    if computer == 'r':
      win()
    elif computer == 's':
      lose()
  elif user == 's':
    if computer == 'p':
      win()
    elif computer == 'r':
      lose()
  else:
      error()

game()

############################################################################################################


############################################################################################################
# Alternative

def altgame():
  user = input("choose 'r' for rock, 'p' for paper, 's' for scisors: ")
  computer = random.choice(['r','p','s'])
  print(f"you chose {label(user)}, the computer chose {label(computer)}...")
  if user == computer:
    print("It's a tie, try again")
    altgame()
  if iswin(user,computer):
    return "you win"
  return "you lose"
  
def iswin(u,c):
  if((u == 'r' and c == 's') or (u == 'p' and c == 'r') or (u == 's' and c == 'p')):
    return True
  return False

print(altgame())

############################################################################################################