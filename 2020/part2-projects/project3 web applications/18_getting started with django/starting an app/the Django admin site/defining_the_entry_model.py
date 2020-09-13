# Defining the Entry Model

# For a user to record what they've been learning about chess and rock climbing, we need to define a model for the kinds of entries users can make in their learning logs. Each entry needs to be associated with a particular topic. This relationship is called a 'many-to-one relationship', meaning many entries can be associated with one topic.

# Here's the code for the 'Entry' model. Place it in your 'models.py' file.

# from django.db import models

# class Topic(models.Model):
#   --snip--

# class Entry(models.Model):
#   """Something specific learned about a topic."""
#   topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#   text = models.TextField()
#   date_added = models.DateTimeField(auto_now_add=True)

# class Meta:
#   verbose_name_plural = 'entries'

#   def __str__(self):
#     """Return a string representation of the model."""
#     return f"{self.text[:50]}..."