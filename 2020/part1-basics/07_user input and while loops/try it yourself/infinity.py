# 7-7 INFINITY

# Write a loop that never ends.

pizza_toppings = [
  'pepperoni', 'cheese', 'pineapple', 'sausage', 'green peppers', 'green pepper', 'hamburger'
]

prompt = "\nType your pizza toppings below."
prompt += "\n(If your topping is not included the program will quit.)\n:  "

topping = ""
while True:
  topping = input(prompt)
  
  if topping.lower() in pizza_toppings:
    print("\nWe have that! Would you like another?\n")
  else:
    print("Sorry we don't have that...goodbye")
