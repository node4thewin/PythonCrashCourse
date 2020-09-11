import unittest
from city_functions import location

class LocationsTestCase(unittest.TestCase):
  """Tests for 'city_functions.py'."""

  def test_city_country(self):
    """Does the output look like 'Santiago, Chile'."""
    formatted_location = location('santiago', 'chile')
    self.assertEqual(formatted_location, 'Santiago, Chile')

if __name__ == '__main__':
  unittest.main()