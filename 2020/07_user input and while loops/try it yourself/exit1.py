
# # Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:

# 1. Use a 'conditional test' in the 'while' statement to stop the loop.

pizza_toppings = [
  'pepperoni', 'cheese', 'pineapple', 'sausage', 'green peppers', 'green pepper', 'hamburger'
]

prompt = "\nType pizza topping here: "
prompt += "\n(Type 'quit' to end program.)\n:  "

topping = ""
while topping != 'quit':
  topping = input(prompt)
  if topping.lower() in pizza_toppings:
    print("\nWe have that! Would you like anything else on your pizza?\n")