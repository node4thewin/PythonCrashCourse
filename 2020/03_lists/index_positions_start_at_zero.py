# INDEX POSITIONS START AT 0, NOT 1

# Python considers the first item in a list to be at position ZERO (0), not position 1.
# This is true of most programming languages, and the reason has to do with how the list
# operations are implemented at a lower level. If you're receiving unexpected results, 
# determine whether you are making a simple off-by-one error. 

# The second item in a list has an index of 1. Using this counting system, you can get any
# element you want from a list by subtracting one from its position in the list. For
# instance, to access the fourth item in a list, you request the item at index 3. The
# following asks for the bikes at index 1 and index 3:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# Python has a special syntax for accessing the last element in a list. By asking for the
# item at index -1, Python always returns the last item in the list:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# This is useful for when you want to access the last item in a list but you don't know how
# long the list is. 

