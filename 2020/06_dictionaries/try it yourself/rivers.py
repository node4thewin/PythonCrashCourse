# 6-5 RIVERS

# Make a dictionary containing three major rivers and the state/country each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {
  'nile': 'egypt',
  'shenandoah': 'virginia',
  'colorado': 'colorado',
  'potomac': 'virginia'
}

# Use a loop to print a sentence about each river, such as the "The Nile runs through Egypt".
for river, location in rivers.items():
  print(f"The {river.title()} River runs through {location.title()}")

# Use a loop to print the name of each river included in the dictionary.
print("\nHere is a list of all the Rivers:\n")
for river in rivers.keys():
  print(river.title())

# Use a loop to print th ename of each country included in the dictionary.
print("\nHere is a list of all the Locations:\n")
for river in set(rivers.values()):
  print(river.title())