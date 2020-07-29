# CHECKING THAT A LIST IS NOT EMPTY

# We've made a simple assumption about every list we've worked with so far; we've assumed that each list has at least one item in it. Soon we'll let users provide the information that's stored in a list, so we won't be able to assume that a list has any items in it each time a loop is run. In this situation, it's useful to check whether a list is empty before runnign a 'for' loop.

# As an example, let's check whether the list of 'requested_toppings' is empty before building the pizza. If the list is not empty, we'll build the pizza just as we did in the previous examples.

requested_toppings = []

if requested_toppings:
  # nested the for loop inside the 'if' statement
  for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
  print("\nFinished making your pizza")

else:  # in case the list is empty
  print("Are you sure you want a plain pizza?")

# This time we start out with an empty list of 'requested_toppings' at line 7. Instead of jumping right into a 'for' loop, we do a quick check at line 11. When the name of a list is used in an 'if' statement, Python returns 'True' if the list contains at least one item; an empty list evaluates at 'False". If 'requested_toppings' passes the conditional test, we run the 'for' loop we used in the previous example. If the conditional test fails, we print a message asking the customer if they really want a plain pizza with no toppings (Line 15).

# The list is empty in this case, so the output asks if the user really wants a plain pizza. If the list wasnt empty, the output will show each requested topping being added to the pizza.