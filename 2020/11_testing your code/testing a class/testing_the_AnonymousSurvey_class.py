# Testing the AnonymousSurvey Class

# Let's write a test that verifies one aspect of the way 'AnonymousSurvey' behaves. We'll write a test to verify that a single response to the survey question is stored properly. We'll use the assertIn() method to verify that the response is in the list of responses after it's been stored:

# go to test_survey.py for the clean version

# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#   """Tests for the class AnonymousSurvey."""

#   def test_store_single_response(self):
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     my_survey = AnonymousSurvey(question)
#     my_survey.store_response('English')
#     self.assertIn('English', my_survey.responses)

# if __name__ == '__main__':
#   unittest.main()

# We start by importing the unittest module and the class we want to test, 'AnonymousSurvey'. We call our test case 'TestAnonymousSurvey', which again inherits from unittest.Testcase (line 10). The first method will verify that when we store a response to the survey quetsion, the response ends up in the survey's list of responses. A good descriptive name for this method is 'test_store_single_response()' (line 13). If this test fails, we'll know from the method name shown in the output of the failing test that there was a problem storing a single response to the survey.

# To test the behavior of a class, we need to make an instance of the class. At line 16 we create an instance called 'my_survey' with the question "What language did you first learn to speak?" We store a single response, 'English', using the store_response() method. Then we verify that the response was stored correctly by asserting that 'English' is in the list 'my_survey.responses' (line 18). When we run 'test_survey.py' the test passes.

# This is good, but a survey is useful only if it generates more than one response. Let's verify that three responses can be stored correctly. To do this, we add another method to 'TestAnonymousSurvey':

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
  """Tests for the class AnonymousSurvey."""

  def test_store_single_response(self):
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    my_survey.store_response('English')
    self.assertIn('English', my_survey.responses)

  def test_store_three_responses(self):
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
      my_survey.store_response(response)
    
    for response in responses:
      self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
  unittest.main()