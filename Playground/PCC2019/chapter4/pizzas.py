# 4-1 Pizzas

# Think of at laeast three kinds of pizza. Make a list and store the
# pizza names in a list, and then use a for loop to print the name
# of each pizza.

favorite_pizzas = ['pepperoni', 'sausage', 'meatlovers', 'pineapple']
for favorite_pizza in favorite_pizzas:
	print(favorite_pizza.upper())

# Modify your 'for' loop to print a sentence using the name of the
# pizza instead of printing just the name. Ex. "I like pepperoni
# pizza".

favorite_pizzas = ['pepperoni', 'sausage', 'meatlovers', 'pineapple']
for favorite_pizza in favorite_pizzas:
	print(f"I friggin love {favorite_pizza.title()} Pizza!")

# Add a line at the end of your program, outside the for loop,
# that states how much y ou like pizza. The output should consist
# of three or more lines about the kinds of pizza you like and
# then an additional sentence, such as I really love pizza.

print("I REALLY love Pizza!!!")


