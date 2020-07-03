# SLICING A LIST
# REMEMBER PYTHON STARTS AT ZERO. 0 means 1 and 1 means 2.

# To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify. To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.

# The following example involves a list of players on a team:

players = ['callie', 'michael', 'andrew', 'otis', 'lola', 'james', 'peter', 'jac']
print(players[0:3])

# The code at line 8 prints a slice of this list, which includes just the first three players. The output retains the structure of the list and includes the first three players on the list.

# You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice at the beginnign of the list:
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list. For example, if you want all items from the third item through the last item, you can start with index 2 and omit the second index:
print(players[2:])

# This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list. Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can output any slice from the end of a list. For example, if we want to output the last three players on the roster, we can use the slice players [-3:]:
print(players[-3:])

# Good thing here is that this will continue to work as the list changes in size.

# TIP - You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.
