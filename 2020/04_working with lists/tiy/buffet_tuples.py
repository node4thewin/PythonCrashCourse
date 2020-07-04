# 4-13 BUFFET

# A buffet-style restaurant offers only basic foods. Think of five simple foods, and store them in a tuple.

simple_menu = ("chicken fried rice", "general tsao's chicken", "beef and broccoli", "egg rolls", "lo mein")

# Use a 'for' loop to print each food the restaurant offers.
print("\nThis is the food the Chinese Restaurant offers:")
for menu in simple_menu:
  print(f"- {menu.title()}")

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a 'for' loop to print each of the items on the revised menu.

print("\nThis is the updated menu:")
simple_menu = ("chicken fried rice", "general tsao's chicken", "sweet and sour chicken", "sesame chicken", "spicy beef", "crispy duck")
for menu in simple_menu:
  print(f"- {menu.title()}")

# Try to modify one of the items, and make sure that Python rejects the change.

simple_menu[0] = ('ballsack')