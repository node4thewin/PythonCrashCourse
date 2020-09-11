# Working with Multiple Files

# Let's add more books to analyze. But before we do, let's move the bulk of this program to a function called 'count_words()'. By doing so, it will be easier to run the analysis for multiple books:

def count_words(filename):
  """Count the approximate number of words in a file."""
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  
  except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
  
  else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# Most of this code is unchanged. We simply indented it and moved it into the body of 'count_words()'. It's a good habit to keep comments up to date when you're modifying a program, so we changed the comment to a doc-string and reworded it slightly (line 6).

# Now we can write a simple loop to count the words in any text we want to analyze. We do this by storing the names of the files we want to analyze in a list, and then we call 'count_words()' for each file in the list. We'll try to count the words for 'Alice in Wonderland', 'Siddhartha', 'Moby Dick', and 'Little Women', which are all available in the public domain. I've intentionally left siddhartha.txt out of the directory containing word_count.py, so we can see how well our program handles a missing file.

filenames = [
  'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'
  ]

for filename in filenames:
  count_words(filename)

# The missing 'siddhartha.txt' has no effect on the rest of the program's execution. Using the 'try-except' block in this example provides two significant advantages. We prevent users from seeing a traceback, and we let the program continue analyzing the texts it's able to find. If we don't catch the 'FileNotFoundError that 'siddhartha.txt' raised, the user would see a full traceback, and the program would stop running after trying to analyze 'Siddhartha'. It would never have analyzed 'Moby Dick' or 'Little Women'.