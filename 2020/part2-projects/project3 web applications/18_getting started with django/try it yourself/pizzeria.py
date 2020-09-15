# 18-4 Pizzeria

# Start a new project called 'pizzeria' with an app called 'pizzas'. Define a model 'Pizza' and a field called name, which will hold name values, such as 'Hawaiian' and 'Meat Lovers'. Define a model called 'Topping', with fields called 'pizza' and 'name'. The 'pizza' field should be a foreign key to 'Pizza', and 'name' should be able to hold values such as 'pineapple', 'Canadian bacon', and 'sausage'.

# Register both models with the admin site, and use the site to enter some pizza names and toppings. Use the shell to explore the data you entered.

# class Pizza(models.Model):
#   """Define a model named Pizza."""
#   pizza = models.CharField(max_length=30)

#   def __str__(self):
#     """Return a string representation of the model."""
#     return self.text

# class Topping(models.Model):
#   """Define a model named Toppings."""
#   toppings = models.CharField(max_length=30)

#   def __str__(self):
#     """Return a string representation of Toppings."""
#     return self.text