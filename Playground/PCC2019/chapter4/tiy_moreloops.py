# TRY IT YOURSELF

# 4-12 - More Loops
# All the previous versions of 'foods.py' have avoided using for
# loops to save space. Pick a version of foods.py and use for loops
# to print.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for my_food in my_foods:
	print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
	print(friend_food.title())

