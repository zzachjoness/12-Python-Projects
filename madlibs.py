import random
print(random.randrange(0,5))

# String cocatenation
engineer = "Zach Jones" # some string variable

# Alternatives
print("hire an " + engineer)
print("hire an {}".format(engineer))
# Top Option
print(f"hire an {engineer}")

adj = "exciting"
verb = "solve problems"
verb2 = "swing"
famous_person = "Tiger"
madlib = f"Computer programming is so {adj}! It makes me so exited all the time becuase \
  I love to {verb}. Stay hyrdated and {verb2} like you are {famous_person}"

print(madlib)

username = input("enter username: ")
print(f"Username is {username}")

class Madlibs:
  def __init__(self, i, m):
    self.inputs = i
    self.madlib = m
  @staticmethod
  def showInputs(i):
    print(i)

One = Madlibs("verb", "paragraph")
print(One.inputs)
print(One.madlib)
One.showInputs("a")

intstring = 6 + '6'
print(intstring)

