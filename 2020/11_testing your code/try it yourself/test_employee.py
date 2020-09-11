# Write a test case for Employee. Write two test methods, test_give_default_raise() and test_give_custom_raise(). Use the setUp() method so you don't have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
  """Test for the class Employee."""

  def setUp(self):
    """
    Initiate a test Employee.
    """
    self.test_employee = Employee('test', 'employee', 86900)
  
  def test_give_default_raise(self):
    """Test Default Raise."""
    self.test_employee.give_raise()
    self.assertEqual(self.test_employee.annual_salary, 91900)

  def test_custom_raise(self):
    """Test Custom Raise."""
    self.test_employee.give_raise(10000)
    self.assertEqual(self.test_employee.annual_salary, 96900)

if __name__ == '__main__':
  unittest.main()
    