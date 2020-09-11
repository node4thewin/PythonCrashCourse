# def get_formatted_name(first, last):
#   """Generate a neatly formatted full name."""
#   full_name = f"{first} {last}"
#   return full_name.title()

# version for failed test below...

# def get_formatted_name(first, middle, last):
#   """Generate a neatly formatted full name."""
#   full_name = f"{first} {middle} {last}"
#   return full_name.title()

# now this is the corrected version so the middle name will pass

def get_formatted_name(first, last, middle=''):
  """Generate a neatly formatted full name."""
  if middle:
    full_name = f"{first} {middle} {last}"
  else:
    full_name = f"{first} {last}"
  return full_name.title()