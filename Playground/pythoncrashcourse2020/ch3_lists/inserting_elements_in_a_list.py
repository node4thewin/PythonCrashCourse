# INSERTING ELEMENTS INTO A LIST

# You can add a new element at any position in your list by using the insert() method.
# You do this by specifying the index of the new element and the value oft he new item.

dogs = ['great dane', 'pug', 'shephard', 'mutt']
print(dogs)

dogs.insert(2, 'pitbull')
print(dogs)

# In this example, the code inserts the value 'pitbull' at the third space on the list.
# As a reminder this is because everything starts at 0. The insert() method opens a
# a space at position "2" and stores the value 'pitbull' at that location. This operation
# shifts every other value in the list one position to the right.


