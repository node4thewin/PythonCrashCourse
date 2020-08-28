# Example from "importing_an_entire_module.py"

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When Python reads this file, the line 'import pizza' tells Python to open the file 'pizza.py' and copy all functions from it into this program. You don't actually see the code being copied between files because Python copies the code behind the scenes just before the program runs. All you need to know is that the any function defined in 'pizza.py' will now be available in 'making_pizzas.py'

# To call a function from an imported module, enter the name of the module you imported, 'pizza', followed by the name of the function 'make_pizza()' separated by a dot (line 3). This code produces the same output as the original program that didn't import a module.