# USING MULTIPLE LISTS

# People will ask for just about anything, especially when it comes to pizza toppings. What if a customer actually wants french fries on their pizza? You can use lists and 'if' statemtns to make sure your input makes sense before you act on it.

# Let's watch out for unusual topping requests before we build a pizza. The followin example defines two lists. The first is a list of available toppings at the pizzeria, and the second is the list of toppings that the user has requested. This time, each item in 'requested_toppings' is checked against the list of available toppings before it's added to the pizza:

available_toppings = [
  'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'
  ]

requested_toppings = [
  'mushrooms', 'french fries', 'extra cheese', 'hamburger'
  ]

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

# At line 7 we define a list of available toppings at this pizzeria. Note that this could be a tuple if the pizzeria has a stable selection of toppings. At line 11 we make a list of toppings that a customer has requested. Note the unusual request, 'french fries'. At line 15 we loop through the list of requested toppings. Inside the loop, we furst check to see if each requested topping is actually in the list of available toppings (line 16). If it is, we add that topping to the pizza. If the requested topping is not in the list of available topping, the 'else' block will run (line 18). The 'else' block prints a message telling the user which toppings are unavailable. This code syntax produces clean, informative output.