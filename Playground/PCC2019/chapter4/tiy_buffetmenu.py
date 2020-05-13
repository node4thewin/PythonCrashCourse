# TRY IT YOURSELF

# A buffet-style restaurant offers only five basic foods. Think of
# five simple foods, and store them in a tuple.


menu_items = (
	'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder', 'salmon burger', 'crab cakes',
	)
# Notice how there is a comma at the end. This may not be necessary
# but it does signify a tuple, especially if there is only one value

# Use a for loop to print each food the restaurant offers.

print("You can choose from the following menu items:")
for item in menu_items:
	print("- " + item)

# The restaurant changes its menu, replacing two of the items with
# different foods. Add a line that rewrites the tuple, and then use
# a for loop to print each of the items on the revised menu.

menu_items = (
	'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder', 'black cod tips', 'king crab legs',
	)

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
	print("- " + item)

