# ACCESSING(INDEXING) ELEMENTS IN A LIST

# Lists are ordered collections, so you can access any element in a list by telling Python
# the position, or index, of the item desired. To access an element in a list, write the
# name of the list followed by the index of the item enclosed in square brackets.

# For example, let's pull out the first bike in the list "bicycles":

bicycles = ['trek', 'huffy', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# You can also use the string methods from Chapter 2 on any element in this list. For example,
# you can format the element 'trek' more neatly by using the title() method:

print(bicycles[0].title())
