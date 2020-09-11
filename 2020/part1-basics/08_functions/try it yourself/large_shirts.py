# 8-4 LARGE SHIRTS

# Modify the 'make_shirt()' function so that shirts are large by default with a message that reads "I love Python". Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size, text='I Love Python'):
  """Display Size and Text of Shirt"""
  print(f"I would like a size {size.title()} shirt.")
  print(f'I would like my size {size.title()} shirt to say "{text}".\n')

make_shirt('large')
make_shirt('medium')
make_shirt('small', 'BACH-MADE')