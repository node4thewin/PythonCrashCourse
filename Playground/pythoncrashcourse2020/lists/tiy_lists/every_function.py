# 3-10 EVERY FUNCTION

# Think of something you could store in a list. For example, you could make a list of mountain,
# rivers, countries, cities, languages, or anything else you'd like. Write a program that creates
# a list containing these items and then uses each function introduced in this chapter at least
# once

family_members = ['cheri mendelsohn', 'brian mendelsohn', 'alex mendelsohn', 'michael mendelsohn', 'erika gerard', 'daniel gerard', 'karen rarick', 'james rarick', 'phillip harvey sr.', 'helen harvey', 'phillip harvey jr.', 'penny clark', 'callie barron', 'otis']
print("ORIGINAL LIST OF FAMILY MEMBERS:")
print(family_members)

# ACCESSING SPECIFIC ELEMENTS IN A LIST
# REMEMBER: Index Positions Start at 0, Not 1

print("\nACCESSING SPECIFIC ITEMS IN A LIST:")
print(family_members[4])
print(family_members[4].title())

# USING INDIVIDUAL VALUES FROM A LIST (and printing them)

print("\nUSING INDIVIDUAL VALUES FROM A LIST:")
message = f"My brother in law is {family_members[5].title()}."
print(message)

# CHANGING, ADDING, AND REMOVING ELEMENTS
print("\n\nCHANGING, ADDING, AND REMOVING ELEMENTS:")

# MODIFYING ELEMENTS IN A LIST
print("\n\tHOW TO CHANGE THE VALUE OF AN ITEM:")
print("\n(Changing Family Member Otis to Otis Barron)")

print("\nOriginal List:")
print(family_members)
family_members[13] = 'otis barron'
print("\nUpdated List:")
print(family_members)

# ADDING ELEMENTS TO A LIST
print("\nADDING ELEMENTS TO A LIST:")

# APPENDING ELEMENTS TO THE END OF A LIST
print("\n\tAPPENDING ELEMENTS TO THE END OF A LIST:")
print("\nAdding Michael:")
family_members.append('michael harvey')
print(family_members)

# INSERTING ELEMENTS INTO A LIST
print("\n\tINSERTING ELEMENTS INTO A SPECIFIC PLACE ON A LIST")
print("\nAdding Xenia Next to Callie:")
family_members.insert(13, 'xenia harvey')
print(family_members)

# REMOVING ELEMENTS FROM A LIST

print("\nREMOVING ELEMENTS FROM A LIST")

# REMOVING AN ITEM USING THE del STATEMENT
print("\n\tREMOVING AN ITEM USING THE del STATEMENT")
print("\nRemoving Cheri:")
del family_members[0]
print(family_members)

# REMOVING AN ITEM USING THE pop() METHOD
print("\n\tREMOVING AN ITEM USING THE pop() METHOD")
print("\nRemoving Alex with pop():")
popped_family_member = family_members.pop(1)
print(family_members)
print("\nPrinting Alex using pop() List:")
print(popped_family_member.title())

# POPPING ITEMS FROM ANY POSITION ON THE LIST
print("\n\tPOPPING ITEMS FROM ANY POSITION ON THE LIST")


