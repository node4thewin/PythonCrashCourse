# REMOVING AN ITEM USING THE POP METHOD

# Sometimes you'll want to use the value of an item after you remove it from a list. For
# example, you might want to get the x and y position of an alien that was just shot down,
# so you can draw an explosion at that position. In a web application, you might want to
# remove a user from a list of active members and then add that user to a list of inactive
# members.

# The pop() method removes the last item in a list...BUT...it lets you work with that item
# after removing it. The term pop comes from thinking of a list as a stack of items and
# popping one item off the top of the stack. In this analogy, the top of a stack corresponds
# to the end of a list.

# Let's pop a shoe from the list of shoes:

shoes = ['nike', 'adidas', 'vibrum', 'converse', 'rainbow']
print(shoes)

popped_shoe = shoes.pop()
print(shoes)
print(popped_shoe)

# We start by defining and printing the list "shoes" then we pop a value from the list and
# store that value in the variable "popped_shoe". We print the list to show it has been
# removed. Then we print the popped value to prove that we still have access to the value
# that was removed.

# The output shows that the value 'rainbow' was removed from the end of the list and is now
# assigned to the variable "popped_shoe".

# This is useful because what if we stored the "shoes" in chronological order and wanted to 
# make a statement about the last "shoe" we bought?

shoes = ['nike', 'adidas', 'vibrum', 'converse', 'rainbow']
last_owned_shoe = shoes.pop()
print(f'The last shoe I wore was a {last_owned_shoe.title()}.')

