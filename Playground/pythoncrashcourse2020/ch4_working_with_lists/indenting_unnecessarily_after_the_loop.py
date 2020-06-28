# INDENTING UNNECESSARILY AFTER THE LOOP

# If you accidentally indent code that should run after a loop has finished, that code will be repeated once for each item in the list. Sometimes this prompts Python to report an error, but often this will result in a logical error.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")
    
    print("Thank you everyone, that was a great magic show.\n")

# Because the line at 10 is indented, it's printed for each person on the list, as shown when executed in the terminal. This is an example of another logical error, similar to the one in "Forgetting to Indent Additional Lines" on page 54.