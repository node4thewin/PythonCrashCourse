# 18-4 Pizzeria

# Start a new project called 'pizzeria' with an app called 'pizzas'. Define a model 'Pizza' and a field called name, which will hold name values, such as 'Hawaiian' and 'Meat Lovers'. Define a model called 'Topping', with fields called 'pizza' and 'name'. The 'pizza' field should be a foreign key to 'Pizza', and 'name' should be able to hold values such as 'pineapple', 'Canadian bacon', and 'sausage'.

# Register both models with the admin site, and use the site to enter some pizza names and toppings. Use the shell to explore the data you entered.

# class Pizza(models.Model):
#   """Define a model named Pizza."""
#   text = models.CharField(max_length=30)

#   def __str__(self):
#     """Return a string representation of the model."""
#     return self.text

# class Topping(models.Model):
#   """Toppings for Pizza, with Foreign Key created."""
#   pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#   text = models.TextField(max_length=100)
#   date_added = models.DateTimeField(auto_now_add=True)

#   class Meta:
#     verbose_name_plural = 'toppings'

#   def __str__(self):
#     """Return a string representation of Toppings."""
#     return self.text