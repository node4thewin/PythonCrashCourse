# MY PIZZAS, YOUR PIZZAS

# Start with your program from Exercie 4-1 (page 56). Make a copy of the list of pizzas, and call it "friend_pizzas". Then do the following:

pizzas = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'buffalo chicken']

friend_pizzas = pizzas[:]

# Add a new pizza to the original list.
pizzas.append('barbecue')

# Add a different pizzas to the list 'friend_pizzas'.
friend_pizzas.append('white')

# Prove that you have two separate lists. Print the message "My favorite pizzas are:" and then use a for loop to print the first list. Print the message "My friend's favorite pizzas are:", and then use a for loop to print the second list. Make sure each new pizzas is stored in the appropriate list.
print("My favorite pizzas are:\n")
for pizza in pizzas:
  print(f"{pizza.title()} Pizza")

print("\nMy friend's favorite pizzas are:\n")
for friend_pizza in friend_pizzas:
  print(f"{friend_pizza.title()} Pizza")


