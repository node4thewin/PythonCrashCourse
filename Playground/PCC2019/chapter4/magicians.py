
# How to do loops. Chapter 4
# Use the for loop when you want to do the same action to
# every item on the list.

# This is messing with simple loop/print schemes:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	print(f"{magician.upper()}")
	print(f"{magician.title()}\n")

# Keep in mind it helps to use the singlar version of whatever
# noun you are using for the sake of simplicity.

	print(f"{magician.title()}, that was a great trick!")

# When you indent multiple calls under the "for" loop then they
# sequentually complete one call after another then on
# to the next item in the list.

	print(f"I can't wait to see your next trick, {magician.title()}")

# Doing Something After a for Loop
# 
# All lines of code after the "for" loop that are not indented are
# executed once without repetition. This sentence is purposely
# as a thank you message after the "for" loop without indentation:

print("Thank, you everyone. That was a great magic show!\n")

# Repeated cleanly without note.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}\n")

print("Thank you everyone. That was a great magic show!")

# Pay attention to indentation errors. These are important with
# large applications and help provide structure. See below for
# some common errors.

magician = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a a great trick")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# This returns Carolina last because the final value is associated
# with 'carolina'. Thus, she is the only one to receive the "looking
# forward to the next trick" message.

# This is known as a LOGICAL ERROR, the code will run but it does
# not display what you're looking for. 

# Here is an example of Indenting Unnecessarily After the Loop
# Accidentally indenting code that should run after a loop is
# finished will be repeated once for each item in the list.
# Sometimes this prompts Python to report an error, but often
# results in a logical error.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

	print("Thank you everyone, that was a great magic show")

# That was another example of a logical error.

# The following is an example of forgetting the Colon:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

