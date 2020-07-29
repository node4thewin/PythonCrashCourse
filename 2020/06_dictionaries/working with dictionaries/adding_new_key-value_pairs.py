# ADDING NEW KEY-VALUE PAIRS

# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. For example, to add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.

# Let's add two new pieces of information to the 'alien_0' dictionary: the alien's x- and y-coordinates, which will help us display the alien in a particular place on the screen. Let's place the alien on the left edge of the screen, 25 pixels down from the top. Because screen coordinates usually start at the upper-left corner of the screen, we'll place the alien on the left edge of the screen by setting the x-coordinate to 0 and 25 pixels from the top by setting its y-coordinate to positive 25, as shown here:

alien_0 = {'color': 'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# We start by defining the same dictionary that we've been working with. We then print this dictionary, displaying a snapshot of its information. At Line 10 we add a new key-value pair to the dictionary: key 'x_position' and value 0. We do the same for key 'y_position' at line 11. When we print the modified dictionary, we see the two additional key-value pairs.