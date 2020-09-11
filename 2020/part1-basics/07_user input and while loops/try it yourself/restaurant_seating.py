# 7-2 RESTAURANT SEATING

# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.

group = input("How many people are in your group? ")
group = int(group)

if group > 8:
  print("\nYou'll have to wait for a table.")
else:
  print("\nYou're table is ready now!")