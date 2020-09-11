# Analyzing Text

# You can analyze text files containing entire books. Many classic works of literature are available as simple text files because they are in the public domain. The texts used in this section come from Project Gutenberg (http://gutenberg.org/). Project Gutenberg maintains a collection of literary works that are available in the public domain, and it's a great resource if you're interested in working with literary texts in your programming projects.

# Let's pull in the text of 'Alice in Wonderland' and try to count the number of words in the text. We'll use the string method split(), which can build a list of words from a string. Here's what 'split()' does with a string containing the title "Alice in Wonderland":

# The split() method separates a string into parts wherever it finds a space and stores all the parts of the string in a list. The result is a list of words from the string, although some punctuation may also appear with some of the words. To count the number of words in 'Alice in Wonderland', we'll use 'split()' on the entire text. Then we'll count the items in the list to get a rough idea of the number of words in the text:

filename = 'alice.txt'

try:
  with open(filename, encoding='utf-8') as f:
    contents = f.read()

except FileNotFoundError:
  print(f"Sorry, the file {filename} does not exist.")
else:
  # Count the approximate number of words in the file.
  words = contents.split()
  num_words = len(words)
  print(f"The file {filename} has about {num_words} words.")

# i moved the file 'alice.txt' to the correct directory, so the 'try' block will work this time. At line 19 we take the string 'contents', which now contains the entire text of 'Alice in Wonderland' as one long string, and use the split() method to produce a list of all the words in the book. When we use 'len()' on this list to examine its length, we get good approximation of the number of words in the original string (line 20). At line 21 we print a statement that reports how many words were found in the file. This code is placed in the 'else' block because it will work only if the code in the 'try' block was executed successfully. The output tells us how many words are in 'alice.txt':

# The count is a little high because extra information is provided by the publisher in the text file used here, but it's a good approximation of the length of 'Alice in Wonderland'.