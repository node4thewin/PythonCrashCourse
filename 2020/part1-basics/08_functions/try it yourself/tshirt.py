# 8-3 T-Shirt

# Write a function called 'make_shirt()' that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, text):
  """Display Size and Text of Shirt"""
  print(f"I would like a size {size.title()} shirt.")
  print(f'I would like my size {size.title()} shirt to say "{text}".\n')

make_shirt('large', 'BACH THAT ASS UP!!!')
make_shirt('small', 'BACH-MADE')