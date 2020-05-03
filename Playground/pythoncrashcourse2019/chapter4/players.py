# Working with Part of a List

# In Chapter 3 you learned how to access simple elements in a list,
# and in this chapter you've been learning how to work through all
# elements in a list. You can also work wtih a specific group of
# items in a list, which Python calls a SLICE (cool term).

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# If you want the second, third and fourth items in a list, you
# would start the slice at index 1 and end at index 4:

print(players[1:4])

# If you omit the first index in a slice, Python automatically
# starts your slice at the beginning of the list:

print(players[:4])

# A similar syntax works if you want a slice that includes the end
# of a list. Example, if you want all items from the third through
# the last item, start with index 2 and omid the second index:

print(players[2:])

# This syntax allows you to output all of the elements from any
# point in your list to the end regardless of the length. Remember
# that negative index returns a distance from the end of the list. 
# See below:

print(players[-3:])

# LOOPING THROUGH A SLICE

# You can use a slice in a 'for' loop if you want to loop through a
# subset of the elements in a list. In the next example we loop
# through the first three players and print their names as part of
# a simple roster:

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team;")
for player in players [:3]:
	print(player.title())


