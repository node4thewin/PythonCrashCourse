# 8-12 Sandwiches

# Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered. Call the functions three times, using a different number of arguments each time.

def sandwich_order(*ingredients):
  """Display a list of items on a sandiwch order."""
  print(f"\nSandwich Ingredients:")
  for ingredient in ingredients:
    print(f" - {ingredient.title()}")

sandwich_order('bacon', 'lettuce', 'tomato')
sandwich_order('avocado', 'lettuce', 'tomato')
sandwich_order('ham', 'american cheese')
