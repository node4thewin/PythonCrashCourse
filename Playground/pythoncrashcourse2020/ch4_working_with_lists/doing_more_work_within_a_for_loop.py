# DOING MORE WORK WITHIN A 'FOR' LOOP

# You can do just about anything with each item in a 'for' loop. Let's build on the previous example by printing a message to each magician, telling them that they performed a great trick:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# The only difference in this code is that at line 7 we compose a message to each magician, starting with that magician's name. The first time through the loop the value of magician is 'alice', so Python starts the first message with the name 'Alice'. The second is 'David' so on and so forth.

# You can also write as many lines of code as you like in the for loop. Every indented line following the line for magician in magicians is considered "inside the loop", and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.

print("\n*** ADDING A SECOND LINE IN THE 'FOR' LOOP THIS TIME.\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

# You can use as many lines as you like in your 'for' loops. In practice you'll often find it useful to do a number of different operations with each item in a list when you use a 'for' loop.