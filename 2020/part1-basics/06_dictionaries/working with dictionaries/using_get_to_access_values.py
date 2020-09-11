# USING get() TO ACCESS VALUES

# Using keys in square brackets to retrieve the value you're interested in from a dictionary might cause one potential problem: if the key you ask for doesn't exist, you'll get an error. Let's see what happens when you ask for the point value of an alien that doesn't have a point value set:

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# You'll learn more about how to handle errors like this in general in Chapter 10. For dictionaries, specifically you can use the get() method to set a default value that will be returned if the requested key doesn't exist. The 'get()' method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn't exist:

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If there's a chance the key you're asking for might not exist, consider using the get() method instead of the square bracket notation above...

# NOTE - If you leave out the second argument in the call to get() and the key doesn't exist. Python will return the value "None.". The special value None means "no value exists." This is not an error: it's a special value meant to indicate the absence of a value. You'll see more uses for None in Chapter 8 (See below for example)

point_value2 = alien_0.get('points')
print(point_value2)