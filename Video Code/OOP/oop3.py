# OOP Part 3

# polymorphism

class Animal:
  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    return "Woof!"

class Cat(Animal):
  def make_sound(self):
    return "Meow!"

def make_animal_sound(animal):
  return animal.make_sound()

# create object
my_dog = Dog()
my_cat = Cat()

print(make_animal_sound(my_dog))
print(make_animal_sound(my_cat))
