def hello_world():
    print("Hello World!")

class Dog:
  def __init__(self, name, breed):
      self.name = name
      self.breed = breed

  def bark(self):
      return f'{self.name} says Woof!'

  def type(self):
      return f'{self.name} is a {self.breed}'

# Creating an instance of the Dog class
my_dog = Dog('Rylie', 'Mini Dachshund')
shawns_dog = Dog('Roman', 'Mastiff')

