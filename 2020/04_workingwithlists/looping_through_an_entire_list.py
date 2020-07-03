# LOOPING THROUGH AND ENTIRE LIST

# You'll often want to run through all entries in a list, performing the same task with each item. For example, in a game you might want to move every element on the screen by the same amount, or in a list of numbers you might want to perform the same statistical operation on every element. Or perhaps you'll want to display each headline from a list of articles on a web-site. When you want to do the same action with every item in a list, you can use Python's "for" loop.

# Let's say we have a list of magician's names, and we want to print out each name in the list. We could do this by retrieving each name from the list individually, but this approach could cause several problems. For one, it would be repetitive to do this with a long list of names. Also, we'd have to change our code each time the list's length changed. A "for" loop avoids both of these issues by letting Python manage these issues internally.

# Let's use a 'for' loop to print out each name in a list of magicians:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# We begin by defining a list like in Chapter 3, then the line below we definte a "for" loop. The for line tells Python to pull a name from the list (magicians), and associate it with the variable "magician". Python then repeats lines 9 and 10, once for each name in the list.

# Here is a good way to start 'for' loops for some things.
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

