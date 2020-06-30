# ORGANIZING A LIST

# Often, your lists will be created in an unpredictable order, because you can't always control
# the order in which your users provide their data. Although this is unavoidable in most
# circumstances, you'll frequently want to present your information in a particular order.
# Sometimes you'll want to preserve the original order of your list, and other times you'll want
# to change the original order. Python provides a number of different ways to organize your
# lists, depending on the situation.

# SORTING A LIST PERMANENTLY WITH THE sort() METHOD

# Python's sort() method makes it relatively easy to sort a list. Imagine we have a list of cars
# and want to change the order of the list to store them alphabetically. To keep the task simple,
# let's assume that all the values in the list are lowercase.

potential_cars = ['jeep', 'ford', 'chevrolet', 'honda', 'mazda']
print(potential_cars)

potential_cars.sort()
print(potential_cars)

# The sort() method changes the order of the list permanently. The cars are now in alphabetical
# order, and we can never revert to the original order

# SORTING IN REVERSE ALPHABETICAL ORDER

# You can also sort this list in reverse alphabetical order by passing the reverse=True to the
# sort() method. The following example sorts the list of cars in reverse alphabetical order:

potential_cars.sort(reverse=True)
print(potential_cars)

# AGAIN the order of the list is permanently changed

# SEE "sorting_a_list_temporarily_with_sorted.py" to see how to maintain the original order of the
# list.