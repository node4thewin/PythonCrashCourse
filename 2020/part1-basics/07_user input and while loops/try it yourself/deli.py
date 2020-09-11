# 7-8 DELI

# Make a list called 'sandwich_orders' and fill it with the names of various sandwiches. Then make an empty list called 'finished_sandwiches'. Loop through the list of sandwich orders and print a message for each order, such as "I made your tuna sandwich". As each sandwich is made, move it to the list of finished sandwiches. After all sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['italian', 'club', 'blt', 'tuna', 'chicken salad', 'roast beef']

finished_sandwiches = []

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()
  if current_sandwich == 'blt': # added this since BLT didnt work in .title()
    print(f"Just made your {current_sandwich.upper()}.")

  else:
    print(f"Just made your {current_sandwich.title()}.")

print("Welp, looks like all of our sandwiches were made!")