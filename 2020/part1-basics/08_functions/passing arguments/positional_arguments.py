# Positional Arguments

# When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called 'positional arguments'.

# To see how this works, consider a function that displays information about pets. The function tells us what kind of animal each pet is and the pet's name, as shown here:

def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'otis')
describe_pet('dog', 'lola')

# The definition shows that this function needs a type of animal and the animal's name (line 7). when we call 'describe_pet()', we need to provide an animal type and a name, in that order. For example, in the function call, the argument 'hamster' is assigned to the parameter 'animal_type' and the argument 'harry' is assigned to the parameter 'pet_name' (line 12). In the function body, these two parameters are used to display information about the pet being described.