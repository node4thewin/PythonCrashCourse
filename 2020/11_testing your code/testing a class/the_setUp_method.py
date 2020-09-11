# The setUp() Method

# In 'test_survey.py' we created a new instance of 'AnonymousSurvey' in each test method, and we created new responses in each method. The unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in each of your test methods. When you include the 'setUp()' method in a 'TestCase' class, Python runs the setUp() method before running each method starting with test_. Any objects created in the 'setUp()' method are then available in each test method you write.

# Let's use 'setUp()' to create a survey instance and a set of responses that can be used in 'test_store_single response()' and test_store_three_responses():

