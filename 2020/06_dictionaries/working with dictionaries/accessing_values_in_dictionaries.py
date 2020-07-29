# ACCESSING VALUES IN A DICTIONARY

# To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:

alien_0 = {'color': 'green'}
print(alien_0['color'])

# This returns the value associated with the key 'color' from the dictionary 'alien_0'. You can have unlimited number of 'key-value pairs' in a dictionary. For example, here's the original 'alien_0' dictionary with two key-value pairs.

alien_0 = {'color': 'green', 'points': 5}

# Now you can access either the color or the point value of 'alien_0'. If a player shoots down this alien, you can look how many points they should earn using code like this:

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Once the dictionary has been defined, the code at Line 14 pulls the value associated with the key 'points' from the dictionary. This value is then assigned to the variable 'new_points'. Line 15 prints a statement about how many points the player just earned.

# If you run this code every time an alien is shot down, the alien's point value will be retrieved.