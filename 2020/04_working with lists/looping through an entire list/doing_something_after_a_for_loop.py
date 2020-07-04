#  DOING SOMETHING AFTER A 'FOR' LOOP

# What happens one a 'for' loop is finished executing? Usually, you'll want to summarize a block of output or move on to other work that your program must accomplish.

# Any lines of code after the 'for' loop that are not indented are executed once without repetition. Let's write a thank you to the group of magicians as a whole, thanking them for putting on an excellent show. To display this group message after all of the individual messages have been printed.

magicians = ['alice', 'david', 'carolina']
# We place the thank you message after the 'for' loop without indentation:
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!\n")

# You'll find this is a good way to summarize what was performed on an entire data set. For example, you might use a 'for' loop to initialize a game by running through a list of characters and displaying each character on the screen. You might then write some additional code after this loop that displays a 'Play Now' button after all the characters have been drawn to the screen.