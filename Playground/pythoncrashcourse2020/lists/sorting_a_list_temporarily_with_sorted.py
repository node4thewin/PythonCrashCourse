# SORTING A LIST TEMPORARILY WITH THE "sorted()" FUNCTION

# To maintain the original order of a list but present it in a sorted order, you can use the
# "sorted()" function. The sorted() function lets you display your list in a particular order
# but doesn't affect the actual order of the list.

# Let's try this function on the list of cars I want to buy.

cars = ['jeep', 'toyota', 'ford', 'subaru', 'honda']

print("\nHere is the original list of car companies I will be considering:")
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# You can see that we are showing that the list has remained in it's original order.

# THE sorted() FUNCTION CAN ALSO ACCEPT A "reverse=True" ARGUMENT IF YOU WANT TO DISPLAY THE LIST
# IN REVERSE ALPHABETICAL ORDER

print('\nHere is the reverse sorted() list:')
print(sorted(cars, reverse=True))
