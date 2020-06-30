# FORGETTING TO INDENT ADDITIONAL LINES

# Sometimes your loop will run without any errors but won't produce the expected result. This can happen when you're trying to do several tasks in a loop and forget to indent properly. 

# For example, this is what happens when we forget to indent the second line in the loop that tells each magician we're looking forward to their next trick:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# The call to print() on line 10 is supposed to be indented, but because Python finds at least one indented line after the 'for' statement, it doesn't report an error. As a result, the first print() call is executed on line 9. The second print() call is not indented, so it is executed only once after the loop has finished running. Because the final value associated with magician is 'carolina', she is the only one who receives the second message.

# This type of error is called a logical error. It is valid code, but the problem occurs in the logic.