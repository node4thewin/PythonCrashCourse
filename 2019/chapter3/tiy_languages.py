# 3-10
# Try to use EVERY function you learned in Chapter Three.
# (Introducting Lists)

languages = ['Spanish', 'English', 'Australian', 'Portuguese', 'French', 'Italian', 'German', 'Dutch', 'Swedish', 'Norwegian']

print(languages)

# Access one Element in a list
# Basically you can pull out a specific object within the list.

print(languages[2])

# Remember you the list starts with [0]. So make sure you
# keep that in mind.
# For example:

print(languages[0])

# Below you will see that I re-did the list towards lowercase
# in order to show the title() method. I think methods can
# only be placed inside functions, not sure yet but there are
# likely a lot. Get familiar!

print(languages[1].lower())
print(languages[2].lower())
print(languages[0].title())
print(f'\n{languages[0].title()}')

# Printing specific Index Positions (Start at 0, not 1)

print(languages[0])

# Take note I added \n or \t to organize my "whitespace"
# Whitespace is any non printing character. These characters
# include spaces, tabs, and end-of-line (\) symbols. Whitespace
# can be used to organize your output so it's easier to read.

# Also showing, "Using Individual Values from a List"

print("\nMy favorite language is Spanish")
print(f"\n\tAgain...my favorite language is {languages[0]}")
print(languages[1])
print(f"\nMy native language is {languages[1]}")

# Showing how to remove and add something to the end
# of the list with .append()

del languages[4]
languages.append('French')

print(languages[-1])
print(f"\n\t{languages[-1]} is definitely my least favorite language.")

print(f'\n\t{languages}\n')

# Inserting elements into specific locations on the list.

languages.insert(1, 'Chinese')
print(f"\n\t{languages[1]} is my second favorite language, sike. It's the worst language.")

# How to use pop(). It is useful when you want to remove an item but
# use it at the same time. REMEMBER using it alone gets the last
# items removed from the list. But you can remove specific locations.

popped_french = languages.pop()
print(f"\n\tMade sure to remove {popped_french} since it is last on the list and the worst language of all time")

print(f"\n\t{languages}")

popped_chinese = languages.pop(1)
print(f"\n\tCan't remove {popped_french} without removing {popped_chinese}. Amirite!?")

print("\n\tHere is the new list!")
print(f'\n\t{languages}\n')

# Example of how to remove an item by value (or what's on the list)
# vs. the position in the list. Use the remove() method.
# aka languages.remove('Australian')

print(f'\nOf course {languages[2]} might as well be {languages[1]}. So we must remove it!\n')

# If you don't know the position of something on the list but
# you know the name use the function/method below.

languages.remove('Australian')

# Remember sometimes you will have the same thing multiple
# times on a list. You willhave to use loops if you want reoccuring
# things to be removed. Covered in Chapter 7.

# Sorting a list with the sort() method, would require a
# languages.sort() call. But remember when using the 
# sort() method the list is permanently sorted. If you want 
# to temporarily sort, use the sorted() function. See Below. 

print('\n\tHere is an original list of the languages I like.\n')
print(languages)

print('\n\tFor those interested here is a sorted list of the languages I like.\n')
print(sorted(languages))

print('\n\tTo prove that the original list still exists...see below.\n')
print(languages)

print('\n\tI can even reverse sort them temporarily. See below!\n')
print(sorted(languages, reverse=True))

# You can use the reverse() method to reverse the original order
# of the list. This means reverse chronological order. When you
# use this it is permanent, but can be reversed by using the same
# reverse() method call again.

print(f"\n\tNow you'll see the list reverse permanently, then reversed again.\n")

languages.reverse()
print(languages)
languages.reverse()
print(languages)

# This is in the orginal order, but obviously takes into account
# the removal and addition of items on the list.

# Use this to print the length of your list.

print(f'{len(languages)}')

# COMPLETED CHAPTER 3!!!!! LEGGOOO!!!!


