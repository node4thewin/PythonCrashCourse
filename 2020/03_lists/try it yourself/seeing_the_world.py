# 3-8 SEEING THE WORLD

# Think of at least five places in the world you'd like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.

locations = ['italy', 'spain', 'new york', 'switzerland', 'greece', 'iceland']

# Print your list in its original order. Don't worry about printing the list neatly, just print
# it as a raw Python list.

print("\nLocations I'd Like To Travel:")
print(locations)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print("\nSorted in Alphabetical Order:")
print(sorted(locations))

# Show that your list is still in its original order by printing it.

print("\nOriginal List:")
print(locations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the
# original list.

print("\nSorted in Reverse Alphabetical Order:")
print(sorted(locations, reverse=True))

# Show that your list is still in its original order by printing it.

print("\nOriginal List:")
print(locations)

# Use reverse() to change the order of your list. Print the list to show that its order has
# changed.

print("\nChanging Order of Original List with reverse():")
locations.reverse()
print(locations)

# Use reverse() to change the order of your list again. Print your list to show that the order of your
# list has changed.

print("\nReverting back to the Original List:")
locations.reverse()
print(locations)

# Use sort() to change your list so that it's stored in alphabetical order. Print the list to show that
# order has been changed.

print("\nUsing sort() to Permanently Sort in Alphabetical Order:")
locations.sort()
print(locations)

# Use sort() to change your list so that it's in reverse alphabetical order. Print the list to show that
# it has been changed.

print("\nUsing sort() to Permanently Sort in Reverse Alphabetical Order:")
locations.sort(reverse=True)
print(locations)
