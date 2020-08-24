# Modifying a List in a Function

# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing you to work efficiently even when you're dealing with large amounts of data.

# Consider a company that creates 3D printed models of designs that users submit. Designs that need to be printed are stored in a list, and after being printed they're moved to a separate list. The following code does this without using functions:

# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodocahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to 'completed_models' after printing.
# while unprinted_designs:
#   current_design = unprinted_designs.pop()
#   print(f"Printing model: {current_design}")
#   completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#   print(completed_model)

# This program starts with a list of designs that need to be printed and an empty list called 'completed_models' that each design will be moved to after it has been printed. As long as designs remain in 'unprinted_designs', the 'while' loop simulates printing each design by removing a design from the end of the list, storing it in 'current_design', and displaying a message that the current design is being printed. It then adds the design to the list of completed models. When the loop is finished running, a list of the designs that have been printed is displayed.

# We can reorganize this code by writing two functions, each of which does one specific job. Most of the code won't change; we're just making it more carefully structured. The first function will handle printing the designs, and the second will summarize the prints that have been made:

def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to 'completed_models' after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Show all the models that were printed."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodocahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# At line 27, we define the function 'print_models()' with two parameters: a list of designs that need to be printed and a list of completed models. Given these two lists, the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models. At line 37 we define the function 'show_completed_models()' with one parameter: the list of completed models. Given this list, 'show_completed_models()' displays the name of each model that was printed.

# This program has the same output as the version without functions, but the code is much more organized. The code that does most of the work has been moved to two separate functions, which makes the main part of the program easier to understand. Look at the body of the program to see how much easier it is to understand what this program is doing:

# unprinted_designs = ['phone case', 'robot pendant', 'dodocahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# We set up a list of unprinted designs and an empty list that will hold the completed models. Then, because we've already defined our two functions, all we have to do is call them and pass them the right arguments. We call 'print_models()' and pass it to the two lists it needs; as expected, 'print_models()' simulates printing the designs. Then we call 'show_completed_models()' and pass it the list of completed models so it can report the models that have already been printed. The descriptive function names allow others to read this code and understand it, even without comments.

# This program is easier to extend and maintain than the version without functions. If we need to print more designs later on, we can simply call 'print_models()' again. If we realize the printing code needs to be modified, we can change the code once, and out changes will take place everywhere the function is called. This technique is more efficient than having to update code separately in several places in the program.

# This program also demonstrates the idea that every function should have one specific job. The first function prints each design, and the second displays the completed models. This is more beneficial than using one function to do both jobs. If you're writing a function and notice the function is doing too many different tasks, try to split the code into two functions. Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.
