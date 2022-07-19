# Python Intro


# 1. Syntax Stuff

# single line comment

# single line comment
# in multiple lines

"""
multi
line
comment
"""

# Indentation

if 5 > 2:
  print("five is greater than 2")


########################################################################################

# 2.0 Variables

# Basic varaible assign
x = 88                            # x is of type int
y = "John"                        # y is of type string
zz = 3.0                          # z is of type float

# variable type can be specificed with "casting"
xx = str(3)                       # xx will be '3'
yy = int(3)                       # yy will be 3
zz = float(3)                     # zz will be 3.0

# we can find the type of a varible with the type() function
print(type(x))
print(type(y))

# Basic Variable Notes
# string varialbes can be initiated by either single of double quotes
# variable names are case sensitive a will not overwrite A
# illegal variables names utilize leading numbers, hyphens, and spaces


# 2.1 Mutliple Variables

# Many values to multiple variables
xf, yf, zf = "Orange", "Banana", "Cherry"

# One value to multiple variables
xs = ys = zs = "Pineapple"


########################################################################################

# 3.0 Strings

# Strings are arrays
string1 = "i love you"
print(string1[0])                 # returns i
for x in string1:
  print(x)
print(string1[len(string1) - 1])  # len() returns length of item
print("love" in string1)          # keyword in checks if char is present in a string, returns bool
print("love" not in string1)     # keyword not in checks if char is not present in string, returns bool


# 3.1 String Methods

string2 = "Hello World"
print(string2[6:11])               # returns string characers 6,7,8,9,10 - strings are arrays, first char = 0

# List of String Methods https://www.w3schools.com/python/python_ref_string.asp


# 3.2 String Concatenation

a = "Hello"
b = "World"
c = a + ' ' + b
print(a + ' ' + b)
print(c)


# 3.3 String Formatting

age = 33
name = "Zach"
text = "My name is {} and I am {} years old"
print(text.format(name,age))      # The format() method takes the passed args, formats them, and places them in the string wehre placeholders {} are

# 3.4 Escape Charaters

txt = "He thought it was \"funny\", she dissagreed."
print(txt)

# \' Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


########################################################################################

# 4.0 Boolean

# True / False case sensitive (must be capitalized)
print(10 > 9)                     # True
print(10 == 9)                    # False
print(10 < 9)                     # False
o = 10
p = 11
if o < p:
  print("I knew it")
if p > 0:
  print("oops I did it again")
print(bool("Hello"))              # Evaluates the string (True)
print(bool(9))                    # Evaluates the number (True)


########################################################################################

# 5.0 Python Arithmetic Operators

g = 10
h = 5
print(g+h)                        # Addition
print(g-h)                        # Subraction
print(g*h)                        # Multiplication
print(g/h)                        # Division
print(g%h)                        # Modulus
print(100%3)                      # Remainder from division (1)
print(g**h)                       # Exponentiation
print(g//h)                       # Floor division
print(101.9//3)                   # Returns 33

# 5.1 Python Assignment Operators

for i in range(6):
  h += 3
  print(h)

texty = "this is the current value of h: {}"
print(texty.format(h))

for i in range(6):
  h -= 3                          #
  print(h)

set1 = {'a','b','c'}
set2 = {'c','b','e'}
set1 &= set2                       # Bitwise AND set1 &= set2 is primarily used to update the intersection of sets
print("set1: ", set1)
print("set2: ", set2)

set3 = {'x','y','z'}
set4 = {'a','b','c'}
set3 |= set4                        # Bitwise OR
print("set3: ", set3)
print("set4: ", set4)


########################################################################################

# 6.0 Python Collections (Arrays)
  # List - a collection which is ordred and changeable. Allows duplicate members
  # Tuple - a colleciton which is ordered and unchangeable. Allows duplicate members
  # Set - a collection which is unordered, unchangeable*, and unindexed. No duplicate members
  # Dictionary - a collection which is ordred ** and changeable. No duplicated members

  # * set items are unchangeable, but you can remove items and add new items
  # ** As of Python 3.7, dictionaries are ordred (whereas earlier they were not)

# 6.1 Python Lists

#list
#used to store multiple items in a single variable
#list items are ordered, changeable, and allow duplicate values
#list items are indexed, the first item has index [0] .... [n]

mylist = ["apple", "banana", "cherry"]
print(mylist, ", and the first item: ", mylist[0])      # Access list items by their index[0:n-1]

# Negative Indexing --> -1 refers to the last item, -2 refers to the 2nd to last item etc.
print('last item of my list: ', mylist[-1] )

# Change list items
mylist[1] = "lemon"

# Add list items
mylist.append("orange")             # list.append() takes exactly one argument

#Insert list items
mylist.insert(1, "grape")

#Remove list items
mylist.pop(1)                       # Removes 2nd item from list
del mylist[0]                       # del keyword removes the specified index, keyword uses brackets
mylist.pop()                        # Removes first item from the list

mylist2 = [1,2,3,4]
del mylist2                         # Deletes the entire list

mylist3 = ['bird','cat','dog']
mylist3.clear()                     # The clear() method empties the list


print("my updated list: ", mylist)
print("my first emptied list: ", mylist3)

########################################################################################

# 6.2 Python Sets

# Sets are used to store multiple items in a single variable
# Set is 1/4 built-in data ytpes in Python used to store collections of data
# The others are List, Tuple, & Dictionary, all with different qualites and usage
# A set is a collection which is unordered, unchangeable, and unindexed
# Note -- sets are unchangeable, but you can remove and add items.

# Speed note - Lists are slighty faster than sets when you want to iterate over the values
# Speed note - sets are significanty faster than lists if you want to check if an itme is contained within it
# cont'd... as sets can only contain unique items
# Speed note - tubes perform in almost exactly the same way as lists, except for their immutability.


# Example

thisset = {"apple", "banana", "razzzberry"}
print(f"this is my set: {thisset}")

# get the length of a set

print(f"this is the length of our set: {len(thisset)}")

# sets can contain mixed data types

set1 = {9,True, False, "haha", 1132, "blue"}

# you can use the set constructor to create a set

set2 = set(("blue", "pink", "green", "purprle"))

# Access set items
for i in set1:
  print(i)

# Check if item is in set2
print("blue" in set1)

# add item to set2
set2.add("orange")

# add items from one set to another set

set1.update(set2)
print(f"new set: {set1}")

# add any iterable
# The object in the update() tmethod does not have to be a set, it can be any iterable object (tubes,list)..
# cont'd... dictionaries, etc.)

new_list = [0,1,5,2,3,4]
set1.update(new_list)
print(f"newnewset: {set1}"
)

set3 = set((1,2,3,4))
set4 = set((True, False))
set3.update(set4)
print(f"set3.update(set4): {set3}")
set5 = set((1,2,3,4))
set6 = set((True, False))
set6.update(set5)
print(f"set6.update(set5): {set6}")
print(f"1 in set6?: {1 in set6})")

########################################################################################

dict_one = [
  {"brand": "ford", 
  "model": "mustang"
  },
  {"brand": "chevy",
  "model": "corvette"
  }]
print(dict_one[0])
print(dict_one[0]["brand"])
print(dict_one[1])
print(dict_one[1]["brand"])






#tuple
#tuples are used to store multiple items in a single variable
#tuples are ordered and unchangeable

mytuple = ("apple", "banana", "cherry")
print(mytuple)
