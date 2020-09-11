# LOOPING THROUGH A SLICE

# You can use a slice in a 'for' loop if you want to loop through a subset of the elements in a list. In the next example we loop through the first three players and print their names as part of a simple roster:

players = ['callie', 'michael', 'andrew', 'otis', 'lola', 'james', 'peter', 'jac']

print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())

# Slices are very useful in a number of situations. For instance, when you're creating a game, you could add a player's final score to a list every time that player finishes playing. You could then get a player's top three scores by sorting the list in decreasing order and taking a slice that includes just the first three scores. When you're working with data, you can use slices to process your data in chunks of a specific size. Or, when you're building a web application, you could use slices to display information in a series of pages with an appropriate amount of information on each page.
