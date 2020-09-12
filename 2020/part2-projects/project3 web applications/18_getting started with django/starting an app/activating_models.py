# Activating Models

# To use our models, we have to tell Django to include our app in the overall project. Open 'settings.py' (int he 'learning_log/learning_log directory); you'll see a section that tells Django which apps are installed and work together in the project:

# --snip--
# INSTALLED_APPS = [
# 'django.contrib.admin',
# 'django.contrib.auth',
# 'django.contrib.contenttypes',
# 'django.contrib.sessions',
# 'django.contrib.messages',
# 'django.contrib.staticfiles',
# ] 
# --snip--

# Add our app to this list by modifying 'INSTALLED_APPS' so it looks like this:

# --snip--
# INSTALLED APPS = [
#  # My apps
#  'learning_logs',
# 
# Default django apps.
# 'django.contrib.admin',
# --snip--
# ]

# Grouping apps together in a project helps to keep track of them as the project grows to include more apps. Here we start a section called 'My apps', which includes only 'learning_logs' for now. It's important to place your own apps before the default apps in case you need to override any behavior of the default apps with your own custom behavior.

# Next, we need to tell Django to modify the database so it can store information related to the model 'Topic'. From the terminal, run the following command:

# (ll_env)learning_log$ python manage.py migrate
# Operations to perform:
# Apply all migrations: admin, auth, contenttypes, learning_logs, sessions 
# Running migrations:
# Applying learning_logs.0001_initial... OK

# Most of the output from this command is identical to the first time we issued the 'migrate' command. The line we need to check appears at line 36, where Django confirms that the migration for 'learning_logs' worked OK.

# Whenever we want to modify the data that Learning Log manages, we'll follow these three steps: 1. modify 'models.py', 2. call 'makemigrations' on learning_logs, and 3. tell Django to 'migrate' the project.