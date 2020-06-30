# 4-1 TRY IT YOURSELF - PIZZAS

# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a 'for' loop to print the name of each pizza.

pizzas = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'buffalo chicken']
# 1. Modify your 'for' loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like "I like pepperoni pizza."
for pizza in pizzas:
  print(f"One of the pizza flavors included was {pizza.title()}.")
print("\nAs you can tell...I really freakin' love pizza.")

