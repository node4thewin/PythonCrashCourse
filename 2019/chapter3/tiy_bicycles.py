#3-1 Names:

friends_harvey = ['kevin dickerson', 'ben alkire', 'melissa', 'kevin howell', 'sam page']

#Remember to close the string methods title(), and close
#other aspects of variables and f-strings

print(friends_harvey[0].upper())
print(friends_harvey[1].upper())
print(friends_harvey[2].upper())
print(friends_harvey[3].upper())

#3-2 Greetings:

friends_harvey = ['kevin dickerson', 'ben alkire', 'melissa', 'kevin howell', 'sam page']
message1 = f'\nMy best friend is {friends_harvey[0].title()}.'
message2 = f'\nThe girl I like is {friends_harvey[-3].title()}.'
message3 = f"\nBen's best friend is {friends_harvey[-1].title()}."
message4 = f'\nMy good friend is {friends_harvey[-2].title()}.'

print(message1, message2, message3, message4)

#3-3 Your Own List:
#Places I Want to Hike

locations_hiking = ['Yosemite', 'Zion National Park', 'Lost River State Park', 'Otter Creek Wilderness']

statement1 = f'\nI dream about going to {locations_hiking[0]}.'
statement2 = f'\nNext weekend I would like to go to {locations_hiking[2]}.'
statement3 = f'\nI would love to camp and hike {locations_hiking[1]}.'

print(statement1, statement2, statement3)
