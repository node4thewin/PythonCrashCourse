# FORGETTING THE COLON

# The colon at the end of a 'for' statement tells Python to interpret the next line as the start of a loop.

magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)

# If you accidentally forget the colon, as shown at line 6, you'll get a syntax error because Python doesn't know what you're trying to do. Although this is an easy error to fix, it's not always an easy error to find. You'd be surprised by the amount of time programmers spend hunting down single-character errors like this. Such errors are difficult to find because we often just see what we expect to see.
