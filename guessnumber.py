import random
# guess computer generated number
a = int(input("choose low end of range: "))
b = int(input("choose high end of range: "))
random_int = random.randint(a,b)            # Return a random integer N such that a <= N <= b
#random_range = random.randrange(a,b)        # Returns a random integer N such that a <= N < b
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

