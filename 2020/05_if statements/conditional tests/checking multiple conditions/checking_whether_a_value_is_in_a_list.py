# CHECKING WHETHER A VALUE IS IN A LIST

# Sometimes it's important to check whether a list contains a certain value before taking an action. For example, you might want to check whether a new username already exists in a list of current usernames before completing someone's registration on a website. In a mapping project, you might want to check whether a submitted location already exists in a list of known locations.

# To find out whether a particular value is already in a list, use the keyword 'in'. Let's consider some code you might write for the pizzeria. We'll make a list of toppings are in the list.

requested_toppings = ['mushrooms', 'onions', 'pineapple', 'pepperoni', 'sausage']
print('mushrooms' in requested_toppings)
print('ground beef' in requested_toppings)

# At line 8 and 9, the keyword 'in' tells Python to check for the existence of 'mushrooms' and 'ground beef' in the list "requested_toppings". This technique is quite powerful because you can create a list of essential values, and then easily check whether the value you're testing matches one of the values in the list.