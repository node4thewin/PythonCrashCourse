# TRY IT YOURSELF

# 4-10 Slices
# Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# Print the message "The first three items in the list are:". Then 
# use a slice to print the first three items from that program's
# list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
players.append('georgie')
players.append('gemini')
players.append('manuel')
players.append('barbara')

print(players)

print("\n\tThe first three players in the team are:")
print(players[:3])

print("\n\tThe three players from the middle of the team are:")
print(players[3:-3])

print("\n\tThe last three players on the team are:")
print(players[-3:])

