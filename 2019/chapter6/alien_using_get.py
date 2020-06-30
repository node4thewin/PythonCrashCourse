# USING GET() TO ACCESS VALUES

# Using keys in square brackets to retrieve the value you're interested in
# from a dictionary might case one potential problem: if the key you ask for
# doesn't exist, you'll get an error:
# Let's see what happens when you ask for the point value of an alien that
# doesn't have a point value set:

alien_0 = {'color': 'green', 'speed': 'slow'}

# If you printed this, it would have resulted in an error.

# You can use the "get()" method to set a default value that will be returned
# if the requested key doesn't exist. YOU WILL LEARN MORE IN CHAPTER 10

# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key doesn't exist:

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
