bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Lists are ordered collections, so you can access any
#element in a list by telling Python the position, 
#or index, of the item desired. Example below.

print(bicycles[0])

#You can also use the string methods from Chapter 2, like
#the title() method:

print(bicycles[0].title())

#INDEX POSITIONS START AT 0, NOT 1
#Python considers the first item in a list to be at
#position 0, not position 1.

print(bicycles[1])
print(bicycles[2])

#There is a special syntax for accessing the last element
#in a list. Asking for index -1 alwasy returns last item.

print(bicycles[-1])

#You can also use - to grab other values from back 2 front.

print(bicycles[-2])

#Using Individual Values from a List

#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

# Try It Yourself

# 3-1 Names: Store the names of a few of your friends in a 
# list called names. Print each person's name by accessing
# each element in the list, one at a time.

names_friends = ['kevin dickerson', 'kevin toney', 'esteban maldonado', 'sam page', 'ian carlin', 'chris conway', 'ben george']
print(names_friends[0])
print(names_friends[1])
print(names_friends[2])
print(names_friends[3])
print(names_friends[4])
print(names_friends[5])
print(names_friends[6])

# 3-2 Greetings: Start with the list you used above, but
# instead of just printing names, print a message to them. The
# text of each message should be the same, but the message
# should be personalized with the person's name.

greeting0 = f"Well hello {names_friends[0].title()}. Why is {names_friends[0+1].title()} such a tool?"
print(greeting0)

greeting1 = f"Well hello {names_friends[1].title()}. Why is {names_friends[1+1].title()} such a tool?"
print(greeting1)
greeting2 = f'Well hello {names_friends[2].title()}. Why is {names_friends[2+1].title()} such a tool?'
print(greeting2)
greeting3 = f'"Well hello {names_friends[3].title()}. Why is {names_friends[3+1].title()} such a tool"'
print(greeting3)
greeting4 = f'Well hello {names_friends[4].title()}. Why is {names_friends[4+1].title()} such a tool?'
print(greeting4)
greeting5 = f'Well hello {names_friends[5].title()}. Why is {names_friends[5+1].title()} such a tool?'
print(greeting5)


