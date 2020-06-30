# REMOVING ELEMENTS FROM A LIST

# Often, you'll want to remove an item or a set of items from a list. For example, when
# a player shoots down an alien from the sky, you'll most likely want to remove it from
# the list of active aliens. Or when a user decides to cancel their account on a web
# application you created, you'll want to remove that user from the list of active users.
# You can remove an item according to its position in the list or according to its value.

# REMOVING AN ITEM USING THE "del" STATEMENT

# If you now the position of the item you want to remove from a list, you can use the "del"
# statement.

farmcrest_plants = ['fig newton', 'basil trio', 'ophelia', 'lemon thyme', 'parsley']
print(farmcrest_plants)

del farmcrest_plants[1]

print(farmcrest_plants)

# You can remove an item from any position in a list using the 'del' statement if you know
# it's "index" aka position.

# YOU CAN NO LONGER ACCESS THE VALUE THAT WAS REMOVED AFTER THE 'del' STATEMENT IS USED

