import unittest
from city_functions_modified import location

class LocationsTestCase(unittest.TestCase):
  """Tests for 'city_functions.py'."""

  def test_city_country(self):
    """Does the output look like 'Santiago, Chile'."""
    formatted_location = location('santiago', 'chile')
    self.assertEqual(formatted_location, 'Santiago, Chile')

# Write a second test called 'test_city_country_population()' that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'. Run test_cities.py again, and make sure this new test passes.

  def test_city_country_population(self):
    """Test whether population can be included."""
    santiago_chile = location('santiago', 'chile', population=5_000_000)
    self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
  unittest.main()