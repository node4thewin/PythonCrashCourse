# A Failing Test

# What does a failing test look like? Let's modify 'get_formatted_name()' so it can handle middle names, but we'll do so in a way that breaks the function for names with just a first and last name, like Janis Joplin.

# Here's a new version of 'get_formatted_name()' that requires a middle name argument:

# Go to name_function.py for a clean version...

def get_formatted_name(first, middle, last):
  """Generate a neatly formatted full name."""
  full_name = f"{first} {middle} {last}"
  return full_name.title()

# This version should work for people with middle names, but when we test it, we see that we've broken the function for people with just a first and last name. This time, running the file 'test_name_function.py' gives this output.

# There's a lot of information here because there's a lot you might need to know when a test fails. The first item in the output is a single E, which tells us one unit test in the test case resulted in an error. Next, we see that 'test_first_last_name()' in NamesTestCase caused an error. Knowing which test failed is critical when your test case contains many unit tests. At Traceback we see a standard traceback, which reports that the function call 'get_formatted_name('janis', 'joplin') no longer works because it's missing a required positional argument. 

# We also see that one unit test was run in 0.000s. Finally we see an additional message that the overall test case failed and that one error occurred when running the test case (FAILED (errors=1)). This information appears at the end of the output so you see it right away; you don't need to scroll up through a long output listing to find out how many tests failed.