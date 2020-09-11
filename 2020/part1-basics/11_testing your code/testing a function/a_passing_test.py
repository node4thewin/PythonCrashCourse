# A Passing Test

# The syntax for setting up a test case takes some getting used to, but once you've set up the test case it's straightforward to add more unit tests for your functions. To write a test case for a function, import the 'unittest' module and the function you want to test. Then create a class that inherits from 'unittest.TestCase', and write a series of methods to test different aspects of you function's behavior.

# Here's a test case with one method that verifies that the function 'get_formatted_name()' works correctly when given a first and last name:

# Go to test_name_function.py for a clean version...

import unittest # this imports the unittest module
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  """Tests for 'name_function.py'."""

  def test_first_last_name(self):
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
  unittest.main()

# First we import 'unittest' and the function we want to test, 'get_formatted_name()'. At line 12 we create a class called 'NamesTestCase', which will contain a series of unit tests for 'get_formatted_name()'. You can name the class anything you want, but it's best to call it something related to the function you're about to test and use the word 'Test' in the class name. This class must inherit from the class 'unittest.TestCase' so Python knows how to run the tests you write.

# NamesTestCase contains a single method that tests one aspect of 'get_formatted_name()'. We call this method 'test_first_last_name()' because we're verifying that names with only a first and last name are formatted correctly. Any method that starts with test_ will be run automatically when we run test_name_function.py. Within this test method, we call the function we want to test. In this example we call 'get_formatted_name()' with the arguments 'janis' and 'joplin', and assign the result to 'formatted_name' (line 17).

# At line 18 we use one of the unittest's most useful features: an 'assert' method. Assert methods verify that a result you received matches the result you expected to receive. In this case, because we know 'get_formatted_name()' is supposed to return a capitalized, properly spaced full name, we expect the value of 'formatted_name' to be 'Janis Joplin'. To check if this is true, we use unittest's 'assertEqual()' method and pass it 'formatted_name' and 'Janis Joplin'. The line 

# self.assertEqual(formatted_name, 'Janis Joplin')

# says, "Compare the value in formatted_name to the string 'Janis Joplin'. If they are equal as expected, fine. But if they don't match, let me know!"

# We're going to run this file directly but it's important to note that many testing frameworks import your test files before running them. When a file is imported, the interpreter executes the file as it's being imported. The 'if' block at line 20 looks at a special variable, __name__, which is set when the program is executed. If this file is being run as the main program, the value of __name__ is set to '__main__'. In this case, we call 'unittest.main()', which runs the test case. When testing framework imports this file, the value of __name__ won't be '__main__' and this block will not be executed.

# When we run 'test_name_function.py', we get the following output...

# The dot on the first line of the output tells us that a single test passed. The next line tells us that Python ran one test, and it took less than 0.001 seconds to run. The final OK tells us that all unit tests in the test case passed.

# This output indicates that the function 'get_formatted_name()' will always work for names that have a first and last name unless we modify the function. When we modify 'get_formatted_name()', we can run this test again. If the test case passes, we know the function will still work for names like Janis Joplin.