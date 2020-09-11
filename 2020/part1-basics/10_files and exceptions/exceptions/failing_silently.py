# Failing Silenty

# In the previous example, we informed our users that one of the files was unavailable. But you don't need to report every exception you catch. Sometimes you'll want the program to fail silently when an exception occurs and continue as if nothing happened. To make a program fail silently, you write a 'try' block as usual, but you explicitly tell Python to do nothing in the 'except' block. Python has a 'pass' statement that tells it to do nothing in a block:

def count_words(filename):
  """Count the approximate number of words in a file."""
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  
  except FileNotFoundError:
    pass
  
  else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

filenames = [
  'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_somen.txt'
  ]

for filename in filenames:
  count_words(filename)

# The only difference between this listing and the previous one is the 'pass' statement at line 12. Now when FileNotFoundError is raised, the code in the 'except' block runs, but nothing happens. No traceback is produced, and there's no output in response to the error that was raised. Users see the word counts for each file that exists, but they don't see any indication that a file wasn't found.

# The 'pass' statement also acts as a placeholder. It's a reminder that you're choosing to do nothing at a specific point in your program's execution and that you might want to do something there later. For example, in this program we might decide to write any missing filenames to a file called 'missing_files.txt'. Our users wouldn't see this file, but we'd be able to read the file and deal with any missing texts.