# Creating Multiple Instances

# You can create as many instances from a class as you need. Let's create a second dog called 'your_dog':

class Dog:
  """A simple attempt to model a dog."""

  def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age

  def sit(self):
    """Simulate the dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My god is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# In this example we create a dog named Willie and a dog named Lucy. Each dog is a separate instance with its own set of attributes, capable of the same set of actions.

# Even if we used the same name and age for the second dog, Python would still create a separate instance from the 'Dog' class. You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.
