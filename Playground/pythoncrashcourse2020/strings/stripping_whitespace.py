# STRIPPING WHITESPACE
# Extra Whitespace can be confusing in your programs. To programmers 'python' and 'python  ' look relatively the same but to a program, they are two
# different strings. Python detects the extra space in 'python' and considers it significant unless you tell it otherwise.

# Whitespace is important because often you'll want to compare two strings to determine whether they are the same. For example, one important instance
# might involve checking people's usernames when they log in to a website. Extra whitespace can be confusing in much simpler situations as well.
# Fortunately, Python makes it easy to eliminate extraneous whitespace from data that people enter.

# Python can look for extra whitespace on the right and left sides of a string. to ensure that no whitespace exist at the right end of a string, use
# the rstrip() method.

# RSTRIP() METHOD

# (to prove this it is best to just open Python3 ih terminal)

favorite_language = 'python  '

# then type...

favorite_language.rstrip()

# then type...

favorite_language

# This shows that favorite_language still means the same thing.

# You can also remove the whitespace 'python   ' from the string permanently, you have to associate the stripped value with the variable name:
# This should be done in Python3 via terminal as well to visualize.

favorite_language = 'python   '
favorite_language = favorite_language.rstrip()
favorite_language

# Changing a variable's value is done often in programming. This is how a variable's value can be updated as a program is executed or in response
# to user input. 

# You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():

favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language

# The above can be shown best using Python3 in the Terminal

# IN THE REAL WORLD, THESE STRIPPING FUNCTIONS ARE USED MOST OFTEN TO CLEAN UP USER INPUT BEFORE IT'S STORED IN A PROGRAM.

