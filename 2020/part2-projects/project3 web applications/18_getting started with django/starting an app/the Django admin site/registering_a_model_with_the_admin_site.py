# Registering a Model with the Admin Site

# Django includes some models in the admin site automatically, such as 'User' and 'Group', but the models we create need to to be added manually.

# When we started the 'learning_logs' app, Django created an 'admin.py' file in the same directory as 'models.py'. Open the admin.py file...

# To register 'Topic' with the admin site, enter the following:

# from django.contrib import admin

# from .models import Topic

# admin.site.register(Topic)

# This code first imports the model we want to register, 'Topic' (line 11). The dot in front of 'models' tells Django to look for models.py in the same directory as 'admin.py'. The code 'admin.site.register()' tells Django to manage our model through the admin site (line 13).

# Now use the superuser account to access the admin site. Go to http://localhost:8000/admin/, and enter the username and password for the superuser you just created. You should see a screen like the one in Figure 18-2. This page allows you to add new users and groups, and change existing ones. You can also work with data related to the 'Topic' model that we just defined.

# NOTE - If you see a message in your browser that the web page is not available, make sure you still have the Django server running in a terminal window. If you don't, activate a virtual environment and reissue the command 'python manage.py runserver'. If you're having trouble viewing your project at any point in the development process,closing any open terminals reissuing the 'runserver' command is a good first troubleshoot step.