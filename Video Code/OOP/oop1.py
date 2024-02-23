# OOP

class Dog:
  def __init__(self, name, age): # constructor
    self.name = name
    self.age = age

  def bark(self):
    return "Woof!"

# create object
my_dog = Dog("Buddy", 3)

# main
print(my_dog)
print(my_dog.name)
print(my_dog.age)

print(my_dog.bark())
