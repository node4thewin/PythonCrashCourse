# ORDER MATTERS IN POSITIONAL ARGUMENTS

# You can get unexpected results if you mix up the order of the arguments in a function call when using positions arguments:

def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')

# In this function call we list the name first and the type of animal second. Because the argument 'harry' is listed first this time, that value is assigned to the parameter 'animal_type'. Likewise, 'hamster' is assigned to 'pet_name'. Now we have a 'harry' named 'hamster'.

# If you get funny results like this, check to make sure the order of the arguments in your function call matches the order of the parameters in the function's definition.