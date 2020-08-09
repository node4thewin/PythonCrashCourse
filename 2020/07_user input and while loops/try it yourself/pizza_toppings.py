# 7-4 PIZZA TOPPINGS

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

prompt = "\n(Type 'quit' at anytime to close the program.)"
prompt += "\nEnter your favorite pizza topping: "

while True:
  topping = input(prompt)

  if topping == 'quit':
    break
  else:
    print(f"Solid choice! {topping.title()} is one of my choices as well.")