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



# create instances of the car class
c1 = Car('toyota','supra','white')
c2 = Car('lexus','gF','blue')
c3 = Car('lexus', 'g350','gold')

# sets are unhashable data types
car_club = {
  Car('honda','type R','blue'),
  Car('honda', 'civic Si', 'white')
}

# the hash function accepts an object and returns the hash value as an integer.
# When you pass an object to the hash() function, Python will execute the __hash__ method of the object
print(hash(c1))
print(hash(c2))
print(hash(c3))

print(hash(car_club))
