# REMOVING KEY-VALUE PAIRS

# When you no longer need a piece of information that's stored in a dictionary, you can use the 'del' statement to completely remove a key-value pair. All 'del' needs is the name of the dictionary and the key that you want to remove.

# For example, let's remove the key 'points' from the alien_0 dictionary along with its value:

alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)

del alien_0['points']
print(alien_0)

# Line 10 tells Python to delet the key'points' from the dictionary 'alien_0' and to remove the value associated with that key as well. The output shows that key 'points' and its value of 5 are deleted from the dictionary, but the rest of the dictionary is unaffected.

# BE AWARE THAT THE KEY-VALUE PAIR IS REMOVED PERMANENTLY
