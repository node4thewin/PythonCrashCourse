# COPYING A LIST

# Often, you'll want to start with an existing list and make an entirely new list based on the first one. Let's explore how copying a list works and examine one situation in which copying a list is useful.

# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

# For example, imagine we have a list of our favorite foods and want to make a separate list of foods that a friend likes. This friend likes everything in our list so far, so we can create their list by copying ours:

my_foods = ['steak', 'tacos', 'pepperoni pizza', 'guacomole']
callie_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(callie_foods)

# At line 9 we make a list of the foods we like called 'my_foods'. At line 10 we make a new list called friend_foods. We make a copy of my_foods by asking for a slice of my_foods without specifying any indices and store the copy in friend_foods. When we print each list, we see that they both contain the same foods.

# To prove that we actually have two separate lists, we'll add a new food to each list and show that each list keeps track of the appropriate person's favorite foods:

my_foods.append('bacon cheeseburgers')
callie_foods.append('crab cakes')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(callie_foods)