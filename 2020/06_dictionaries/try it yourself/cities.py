# 6-11 CITIES

# Make a dictionary called 'cities'. Use the name of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its appropriate population, and one fact about that city. The keys for each city's dictionary should be something like 'country', 'population', and 'fact'. Print the name of each city and all of the information you have stored about it.

# Make a dictionary inside a dictionary

cities = {
  'paris': {
    'country': 'france',
    'population': 2148000,
    'fact': 'Known for its cafe culture and designer boutiques along the Rue du Faubourg Saint-Honoré'
  },

  'seoul': {
    'country': 'south korea',
    'population': 9776000,
    'fact': "It's a huge metropolis where modern skyscrapers and pop culture meet Buddhist Temples, palaces, and street markets."
  },

  'london': {
    'country': 'england',
    'population': 8982000,
    'fact': 'The capitol of England and the United Kingdom, is a 21st-century city with history stretching back to Roman times.'
  },
}

print("Check out this interesting information:")

for city, city_info in cities.items():
  print(f"\nCity: \t\t{city.title()}")
  country = f"{city_info['country']}"
  population = f"{city_info['population']}"
  fact = f"{city_info['fact']}"

  print(f"Country: \t{country.title()}")
  print(f"Population: \t{population.title()}")
  print(f"Fact: \t\t{fact}")