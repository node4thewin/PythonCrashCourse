# Importing an Entire Module

# To start importing functions, we first need to create a module. A 'module' is a file ending in .py that contains the code you want to import into your program. Let's make a module that contains the function 'make_pizza()'. To make this module, we'll remove everything from the file 'pizza.py' except the function 'make_pizza()'.

def make_pizza(size, *toppings):
  """Summarize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

# Now we'll make a separate file called making_pizzas.py in the same directory as pizza.py. This file imports the module we just created and then makes two calls to 'make_pizza()':

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When Python reads this file, the line 'import pizza' tells Python to open the file 'pizza.py' and copy all functions from it into this program. You don't actually see the code being copied between files because Python copies the code behind the scenes just before the program runs. All you need to know is that the any function defined in 'pizza.py' will now be available in 'making_pizzas.py'

# To call a function from an imported module, enter the name of the module you imported, 'pizza', followed by the name of the function 'make_pizza()' separated by a dot (line 15). This code produces the same output as the original program that didn't import a module.

# This first approach to importing, in which you simply write 'import' followed by the name of the module, makes every function from the module available in you program. If you use this kind of import statement to import an entire module named 'module_name.py', each function in the module is available through the following syntax:

# module_name.function_name()