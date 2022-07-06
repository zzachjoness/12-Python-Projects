import random
random_num = random.randrange(0,5)

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

#if random_num == 0:
inputs = [input("adjective: "),input("noun: "),input("plural noun: "),input("number: "),input("adjective: "),input("verb ending in \"s\": "),input("adjective: "),input("noun: "),input("noun: "),input("noun: "),input("noun: "),input("verb ending in \"s\": "),input("noun: "),input("adjective: "),input("noun: "),input("plural noun: "),input("adjective: "),input("noun: ")]
newline = "\n"
madlib = f"Lewis Caroll's classic, Alice's Adventures in Wonderland, as well as its {inputs[0]} sequel, \
{newline}Through the Looking {inputs[1]}, have enchanted both the young and the old {inputs[2]} for the last {inputs[3]} years. \
{newline}Alice's {inputs[4]} adventures being when she {inputs[5]} down a/an {inputs[6]} hole and lands in a strange topsy-turvy \
{newline}{inputs[7]}. There she discovers she can become a tall {inputs[8]} or a small {inputs[9]} simply by nibbling on alternate \
{newline}sides of a magic {inputs[10]}. In her travels through Wonderland, Alice {inputs[11]} such remarkable characters as \
{newline}the White {inputs[12]}, the {inputs[13]} Hatter, the Cheshire {inputs[14]}, and even the Queen of {inputs[15]}. Unfortunately, Alice's \
{newline}adventures come to a/an {inputs[16]} end when Alice awakens from her {inputs[17]}."
  
#18 inputs
print(madlib)