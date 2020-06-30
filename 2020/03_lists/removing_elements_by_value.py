# REMOVING AN ITEM BY VALUE

# Sometimes you won't know the position of the value you want to remove from a list. If you
# only know the value of the item you want to remove, you can use the "remove()" method.

# For example, let's say we want to remove the value 'bullett' from a list of my favorite
# whiskeys.

fav_whiskeys = ['bullett', 'four roses', "angel's envy"]
print(fav_whiskeys)

fav_whiskeys.remove('bullett')
print(fav_whiskeys)

# The code tells Python to figure out where 'bullett' appears in the list and remove that
# element. You can also use the remove() method to work with a value that's being removed
# from a list. Let's remove the value 'bullett' and print a reason for removing it from the
# list:

fav_whiskeys = ['bullett', 'four roses', "angel's envy"]
print(fav_whiskeys)

not_good = 'bullett'
fav_whiskeys.remove(not_good)
print(fav_whiskeys)

print(f"\n{not_good.title()} is a crap whiskey...not good at all.")
