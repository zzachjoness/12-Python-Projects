import random

############################################################################################################
# User sets range, computer selects random number

a = int(input("choose low end of range: "))
b = int(input("choose high end of range: "))

random_int = random.randint(a,b)            # Return a random integer N such that a <= N <= b
random_range = random.randrange(a,b)        # Returns a random integer N such that a <= N < b

print(f"the computer has selected a random integer between {a} and including {b}")

def test():
  guess = int(input("guess a number: "))
  while guess != random_int: 
    if guess > random_int:
      print(f"your guess of {guess} is too high")
      guess = int(input("guess a number: "))
    elif guess < random_int:
      print(f"your guess of {guess} is too low")
      guess = int(input("guess a number: "))
  print(f"hell yeah, your guess of {guess} is correct")

test()

############################################################################################################


############################################################################################################
# User selects "secret number", computer has to guess number based upon High / Low feedback

secret_number = int(input("select your secret number, x (-1000 <= x <= 1000): "))
print(f"the computer will randomly guess your secret number({secret_number}), based on high or low feedback, how many attempts do you think it will take?")
user_guess = int(input("attempts guess: "))

def pcguess(high = 1000,low = -1000):
  high = int(high)
  low = int(low)
  pcintguess = random.randint(low,high)
  return pcintguess, high, low

def pcfindnumber():
  n = 0
  pcintguess, high, low = pcguess()
  while pcintguess != secret_number:
    n += 1
    if pcintguess < secret_number:
      print(f"the computer guessed {pcintguess} on attempt {n}")
      pcintguess, high, low = pcguess(high, pcintguess)
    if pcintguess > secret_number:
      print(f"the computer guessed {pcintguess} on attempt {n}")
      pcintguess, high, low = pcguess(pcintguess, low)
  print(f"the computer guessed {pcintguess} on attempt {n}")
  print(f"wow, very smart, the pc guessed your \"secret number\" in only {n} attempts")

pcfindnumber()

############################################################################################################