# define the Car class with attribues brand, model, & color
# our car class supports equality based on brand and is hashable

class Car:
  def __init__(self,brand,model,color):
    self._brand = brand
    self.model = model
    self.color = color

  @property
  def brand(self):
    return self._brand
  
  # if a class overrides the __eq__ method, the objects of the class become unhashable.
  # this means that you won't be able to use the objects in a mapping type.
  # for example, you will not be able to use them as keys in a dictionary or elements in a set.
  def __eq__(self,other):
    return isinstance(other, Car) and self.brand == other.brand
  
  # By default, the __hash__ method uses the objects identity and the __eq__ reutnrs True if two objects
  # are the same. To override this default behavior, you can implement the __eq__ and __hash__.
  def __hash__(self):
    return hash(self.brand)

  # The __repr__ is a special method used to represent a class's objects as a string.
  # Return a string containing a printable represenation of an object
  # It is sometimes useful to be able to access this operation as an ordinary function
  def __repr__(self):
    return f'Car(brand={self.brand})'
    #return f'Cars(brand={self.brand}, model={self.model}, color={self.color})'
  



# create instances of the car class
c1 = Car('toyota','supra','white')
c2 = Car('lexus','gF','blue')
c3 = Car('lexus', 'g350','gold')
c4 = Car('honda', 'type r','blue')
c5 = Car('honda', 'civic','blue')

# sets are unhashable data types
car_club = set([c4,c5])
set([c4,c5])

# the hash function accepts an object and returns the hash value as an integer.
# When you pass an object to the hash() function, Python will execute the __hash__ method of the object
print(hash(c1))
print(hash(c2))
print(hash(c3))
print(c2 == c3)
print(set([c4,c5]))
print(car_club)
repr(car_club)


############################################################################################################

#class practice 2

class Myclass:
  def __init__(this,a,b):
    this.a = a
    this.b = b
  
  def __eq__(this,other):
    return this.a == other.a
  
  def __hash__(this):
    return hash(this.a)

  def __repr__(this):
    return f'Myclass(a={this.a}, b={this.b})'

one = Myclass(1,2)
two = Myclass(2,3)
three = Myclass(3,4)
four = Myclass(3,5)
garage_2 = (Myclass(1,2),Myclass(1,3))

print(hash(one))
print(hash(two))
print(hash(three))
print(hash(four))
print(hash(garage_2[0]))
print(hash(garage_2[1]))
print(garage_2)