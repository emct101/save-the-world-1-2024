# OOP Part 2

class Animal:
  def __init__(self, species):
    self.species = species

  def make_sound(self):
    pass

class Dog(Animal): # inheritance
  def __init__(self, name):
    super().__init__("Dog") # superclass
    self.name = name

  def make_sound(self):
    return "Woof!"

class Cat(Animal): # inheritance
  def __init__(self, name):
    super().__init__("Cat") # superclass
    self.name = name

  def make_sound(self):
    return "Meow!"

# create object
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

# main
print(my_dog.make_sound())
print(my_cat.make_sound())
