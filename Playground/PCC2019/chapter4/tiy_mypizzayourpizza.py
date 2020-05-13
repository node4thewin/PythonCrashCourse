# TRY IT YOURSELF

# 4-11 My Pizzas, Your Pizzas:
# Start with your program from 4-1 (pizzas.py)
# Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:

# 1. Add a new pizza to the original list.

my_pizzas = ['pepperoni', 'sausage', 'meatlovers', 'pineapple']
friend_pizzas = my_pizzas[:]

my_pizzas.append('barbeque chicken')

# 2. Add a different pizza to the list of friend_pizzas

friend_pizzas.append('veggie')

# 3. Prove that you have two separate lists. Print the message
# "My favorite pizzas are:", and then use a for loop to print the
# first list. Then print the message "My friend's favorite pizzas
# are:", and then us a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

print("\nMy favorite pizzas are:")
for my_pizza in my_pizzas:
	print(my_pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza.title())



