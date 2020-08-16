# MULTIPLE FUNCTION CALLS

# You can call a function as many times as needed. Describing a second, different pet requires just one more call to 'describe_pet()':

def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'otis')
describe_pet('dog', 'lola')

# In this second function call, we pass 'describe_pet()' the arguments 'dog' and 'otis'. As with the previous set of arguments we used, Python matches 'dog' with the parameter 'animal_type' and 'otis' with the parameter 'pet_name'.

# As before, the function does its job, but this time it prints values for a dog named Otis. Now we have a dog named Otis and another dog named Lola.

# Calling a function multiple times is a very efficient way to work. The code describing a pet is written once in the function. Then, anytime you want to describe a new pet, you call the function with the new pet's information. Even if the code for describing a pet were to expand to ten lines, you could still describe a new pet in just one line by calling the function again.

# You can use as many positional arguments as you need in your functions. Python works through the arguments you provide when calling the function and matches each one with the corresponding parameter in the function's definition.

# You can use as many positional arguments as you need in your functions. Python works through the arguments you provide when calling the function and matches each one with the corresponding parameter in the function's definition.