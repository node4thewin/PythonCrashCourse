# A Variety of Assert Methods

# Python provides a number of 'assert' methods in the 'unittest.TestCase' class. As mentioned earlier, assert methods test whether a condition you believe is true at a specific point in your code is indeed true. If the condition is true as expected, your assumption about how that part of your program behaves is confirmed; you can be confident that no errors exist. If the condition you assume is true is actually not true, Python raises an exception.

# Table 11-1 describes six commonly used assert methods. With these methods you can verify that returned values equal or don't equal expected values, that values are 'True' or 'False', and that values are 'in' or 'not in' a given list. You can use these methods only in a class that inherits from 'unittest.TestCase', so let's look at how we can use one of these methods in the context of testing an actual class.

# Method                      Use

# assertEqual(a, b)           Verify that a == b
# assertNotEqual(a, b)        Verify that a != b
# assertTrue(x)               Verify that x is True
# assertFalse(x)              Verify that x is False
# assertIn(item, list)        Verify that 'item' is in 'list'
# assertNotIn(item, list)     Verify that 'item' is not in 'list'