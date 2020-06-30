cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# Sort will put the list in alphabetical order
# You can also sorty this list in reverse alphabetical
# order by passing the argument reverse=True to the sort()
# method. The following example sorts the list of cars in
# reverse alphabetical order:

cars.sort(reverse=True)
print(cars)

# This is how to sort a list TEMPORARILY. 

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
# Notice the sorted() call inside the print() call.
# Also notice below, the reverse=True sorted() call. 
# Make sure to to have the lists first so it knows what
# to reverse.

print("\nHere is the reverse-sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Notice that the reverse() doesn't sort backward
# alphabetically; it simply reverses the order of the list.
# It is also a permanent change, but you can reverse the
# order of the list again in order to fix it.

cars.reverse()
print(cars)

# Finding the Length of a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
