# Accessing Attributes

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

print(f"My dog's name is {my_dog.name}.")
print(f"My god is {my_dog.age} years old.")

# To access the attributes of an instance, you use dot notation. At line 21 we access the value of my_dog's attribute 'name' by writing:

# my_dog.name

# Dot notation is often used in Python. This syntax demonstrates how Python finds an attribute's value. Here Python looks at the instance 'my_dog' and then finds the attribute 'name' associated 'my_dog'. This is the same attribute referred to as 'self.name' in the class 'Dog'. At line 22 we use the same approach to work with the attribute 'age'.

# The output is a summary of what we know about 'my_dog'.