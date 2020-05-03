# Copying a List

# Sometimes you'll want to start with an existing list and make an
# entirely new one based on the first one.

# In order to copy a list, you can make a slice that includes the
# entire original list by omitting the first index and the second
# index ([:]). This will tell Python to make a slice that starts
# with the first and ends with the last item, thus a copy of the
# entire list.

# Imagine you have a list of your favorite foods and want to make
# a separate list of foods that a friend likes. This friend likes
# everything in our list so far, so we can create their list by
# copying ours:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Now in order to prove that we have two separate lists...we'll
# add a new food to each list and show that each list keeps track
# of the appropriate person's favorite foods:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Make sure to understand that these two lists carry on independently.

# HERE IS AN EXAMPLE OF WHAT DOESNT WORK!!! We can't just set
# friend_foods = my_foods because then both lists will be joined
# together and edited as one.

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:

print("\nThis is an example of the lists not working!!!\n")
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# This = syntax tells Python to associate the new variable
# 'friend_foods' with the list that is already associated with 
# 'my_foods', so now both variables point to the same list.

# NOTE - if you're trying to work with a copy of a list and you see
# unexpected behavior, make sure you are copying the list using a
# slice, as we did in the first example.



