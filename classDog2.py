
"""Classes can also have class attributes, created by assigning variables within the body of the class. These can be accessed either from instances of the class, or the class itself."""

class Dog:
  legs = 4
  def __init__(self, name, color):
    self.name = name
    self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)