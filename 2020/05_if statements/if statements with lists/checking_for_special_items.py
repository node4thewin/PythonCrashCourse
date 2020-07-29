# CHECKING FOR SPECIAL ITEMS

# This chapter began wtih a simple example that showed how to handle a special value like 'bmw', which needed to be printed in a different format than other values in the list. Now that you have a basic understanding of conditional tests and 'if' statements, let's take a closer look at how you can watch for special values in a list and handle those values appropriately.

# Let's continue with the pizzeria example. The pizzeria displays a message whenever a topping is added to your pizza, as it's being made. The code for this action can be written very efficiently by making a list of toppings the customer has requested and using a loop to announce each topping as it's added to the pizza:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!\n")

# The output is straightforward because it's just a simple 'for' loop. BUT...what if the pizzeria runs out of green peppers? An 'if' statement inside the 'for' loop can handle this situation appropriately:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

print("\tExample 'for' loop with 'if' Statement\n")
for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print("Our bad! We are out of green peppers right now.")
  else:
    print(f"Adding {requested_topping}.")

print("\nYour pizza is complete!")

# This time we check each requested item before adding it to the pizza. The code at Line 19 checks to see if the person requested green peppers. If so, we display a message informing them why they can't have green peppers. The 'else' block at Line 22 ensures that all other toppings will be added to the pizza.