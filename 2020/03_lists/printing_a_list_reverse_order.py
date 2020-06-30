# PRINTING A LIST IN REVERSE ORDER

# To reverse the original order of a list, you can use the reverse() method. If we originally
# stored the list of cars in chronological order according to when we owned them, we could easily
# rearrange the list into reverse chronicological order:

cars = ['jeep', 'toyota', 'ford', 'subaru', 'honda']
print(cars)

cars.reverse()
print(cars)

# Notices that reverse() doesn't sort backward alphabetically; it simply reverses the order of the
# list.

# The reverse() method PERMANENTLY changes the order of the list...BUT...you can simply use the
# reverse() to the same list a second time to get the original order.

cars.reverse()
print(cars)
