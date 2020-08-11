# MULTIPLE FUNCTION CALLS

# You can call a function as many times as needed. Describing a second, different pet requires just one more call to 'describe_pet()':

def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'otis')
describe_pet('dog', 'lola')

# In this second function call, we pass 'describe_pet()' the arguments 'dog' and 'otis'. As with the previous set of arguments we used, Python matches 'dog' with the parameter 'animal_type' and 'willie' with the parameter 'pet_name'.

