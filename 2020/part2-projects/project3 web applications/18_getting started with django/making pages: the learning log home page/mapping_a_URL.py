# Mapping a URL

# Users request pages by entering URLs into a browser and clicking links, so we'll need to decide what URLs are needed. The home page URL is first: it's the base URL people use to access the project. At the moment the base URL, 'http://localhost:8000/', returns the default Django site that lets us know the project is set up correctly. We'll change this by mapping the base URL to Learning Log's home page.

# In the main 'learning_log' project folder, open the file 'urls.py'. Here's the code you should see:

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#   path('admin/', admin.site.urls),
# ]

# The first two lines import a module and a function to manage URLs for the admin site (line 7). The body of the file defines the 'urlpatterns' variable (line 10). In this 'urls.py' file, which represents the project as a whole, the 'urlpatterns' variable includes sets of URLs from the apps in the project. The code at line 11 includes the module 'admin.site.urls', which defines all the URLs that can be requested from the admin site.

# We need to include the URLs for learning_logs, so add the following:

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#   path('admin/', admin.site.urls),
#   path('', include('learning_logs.urls')),
# ]

# We've added a line to include the module 'learning_logs.urls' at line 23. The default 'urls.py' is in the 'learning_log' folder; now we need to make a second 'urls.py' file in the 'learning_logs' folder. Create a new Python file and save it as 'urls.py' in 'learning_logs', and enter this code into it:

# """Defines URL pattersn for learning_logs."""

# from django.urls import path

# from . import views

# app_name = 'learning_logs'
# urlpatterns = [
#   # Home page
#   path('', views.index, name='index'),
# ]

# To make it clear which 'urls.py' we're working in, we add a docstring at the beginning of the file (line 28). We then import the 'path' function, which is needed when mapping URLs to views (line 30). We also import the 'views' module (line 32); the dot tells Python to import the 'views.py' module from the same directory as the current 'urls.py' module. The variable 'app_name' helps Django distinguish this 