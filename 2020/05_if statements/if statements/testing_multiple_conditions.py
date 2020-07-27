# TESTING MULTIPLE CONDITIONS

# The 'if-elif-else' chain is powerful, but it's only appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, because it's efficient and allows you to test for one specific condition.

# However, sometimes it's important to check all of the conditions of interest. In this case, you shuold use a series of simple 'if' statements with no 'elif' or 'else' blocks. This technique makes sense when more than once condition could be 'True', and you want to act on every condition that is 'True'.

# Let's reconsider the pizzeria example. If someone requests a two-topping pizza, you'll need to be sure to include both toppings on their pizza:

requested_toppings = ['mushrooms', 'extra cheese']
print("What would you like on your pizza?\n")

if 'mushrooms' in requested_toppings:
  print("\tAdding mushrooms.")
if 'pepperoni' in requested_toppings:
  print("\tAdding pepperoni.")
if 'extra cheese' in requested_toppings:
  print("\tAdding extra cheese.")

print("\nFinished making your pizza!")

# We start at Line 9 with a list containing the requested toppings. The 'if' statement at Line 12 checks to see whether the person requested mushrooms on their pizza. If so, a message is printed confirming that topping. The test for pepperoni at Line 14 is another simple 'if' statement, not an 'elif' or 'else' statement, so this test is run regardless of whether the previous test passed or not. The code at Line 16 checks whether extra cheese was requested regardless of the results from the first two tests. These three independent tests are executed every time this program is run.

# Because every condition in this example is evaluated, both mushrooms and extra cheese are added to the pizza.

# This code would not work properly if we used an 'if-elif-else' block, because the code would stop running after only one test passes. The test for 'mushrooms' is the first test to pass, so mushrooms are added to the pizza, However the values 'extra cheese' and 'pepperoni' are never checked, because Python doesn't run any tests beyond the first test that passes in an 'if-elif-else' chain. The customer's first topping will be added but all of the other toppings would not.

requested_toppings = ['mushrooms', 'extra cheese']
print("\nThis is the example of 'if-elif-elif' version that doesn't work.\n")

if 'mushrooms' in requested_toppings:
  print("\tAdding mushrooms.")
elif 'pepperoni' in requested_toppings:
  print("\tAdding pepperoni.")
elif 'extra cheese' in requested_toppings:
  print("\tAdding extra cheese.")

print("\nFinished making your pizza!")

