# 7-9 NO PASTRAMI

# Using the list 'sandwich_orders' from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a 'while' loop to remove all occurences of 'pastrami' from 'sandwich_orders'. Make sure no pastrami sandwiches end up in 'finished_sandwiches'.

sandwich_orders = ['italian', 'pastrami', 'club', 'blt', 'tuna', 'chicken salad', 'roast beef', 'pastrami', 'pastrami']
finished_sandwiches = []

print("FYI the deli has run out of Pastrami.")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

while sandwich_orders:
  current_order = sandwich_orders.pop()

  if current_order == 'blt':
    print(f"Just made your {current_order.upper()} sandwich.")
  
  else:
    print(f"Just made your {current_order.title()} sandwich.")

