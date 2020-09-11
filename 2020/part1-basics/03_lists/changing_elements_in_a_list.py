# CHANGING, ADDING, AND REMOVING ELEMENTS

# Most lists you create will be dynamic, meaning you'll build a list and then add and
# remove elements from it as your program runs its course. For example, you might create
# a game in which a player has to shoot aliens out of the sky. You could store the initial
# set of aliens in a list and then remove an alien from the list each time one is shot down.
# Each time a new alien appears on the screen, you add it to the list. Your list of aliens
# will increase and decrease in length throughout the course of the game.

# CHANGING ELEMENTS IN A LIST

# The syntax for changing an element is similar to the syntax for accessing an element in a
# list. To change an element, use the name of the list followed by the index of the element
# you want to change, and then provide the new value you want that item to have.

# For example, let's say we have a list of motorcycles, and the first item in the list is 'honda'.
# How would we change the value of this first item?

motorcycles = ['honda', 'yamaha', 'suzuki', 'indian', 'ducati']
print(motorcycles)

motorcycles[0] = 'titan'
print(motorcycles)

# As you can see when you execute the code, 'honda' has been replaced by 'titan'. The output
# shows that the first item has indeed been changed, and the rest of the list remains the same.

# SEE ADDING ELEMENTS TO A LIST NEXT
