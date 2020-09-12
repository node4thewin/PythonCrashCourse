# Creating a Virtual Environment

# To work with Django, we’ll first set up a virtual environment. A virtual environment is a place on your system where you can install packages and isolate them from all other Python packages. Separating one project’s libraries from other projects is beneficial and will be necessary when we deploy Learning Log to a server in Chapter 20.

# Create a new directory for your project called learning_log, switch to that directory in a terminal, and enter the following code to create a virtual environment:

# learning_log$ python3 -m venv ll_env
# learning_log$ python3 -m venv ll_env

# Here we’re running the venv virtual environment module and using it to create a virtual environment named ll_env (note that this is ll_env with two lowercase Ls, not two ones). If you use a command such as python3 when running programs or installing packages, make sure to use that command here.