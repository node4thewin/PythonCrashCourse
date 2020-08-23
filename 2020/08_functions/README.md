# Functions
In this chapter you'll learn to write 'functions', which are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you've defined in a function, you call the function responsible for it. If you need to perform that task multiple times throughout your program, you don't need to type all the code for the same task again and again; you just call the function dedicated to handling the task, and the call tells Python to run the code inside the function. You'll find that using functions makes your programs easier to write, read, test, and fix.

In this chapter you'll also learn ways to pass information to functions. You'll learn how to write certain functions whose primary job is to display information and other functions designed to process data and return a value or set of values. Finally, you'll learn how to store functions in separate files called 'modules' to help organize your main program files.

# Arguments and Parameters

In 'passing_information_to functions.py' we used the 'greet_user()' function, and defined 'greet_user()' to require a value for the variable 'username'. Once we called the function and gave it the information (a person's name), it printed the right greeting.

The variable 'username' in the definition of 'greet_user()' is an example of a 'parameter', a piece of information the function needs to do its job. The value 'jesse' in 'greet_user('jesse') is an example of an 'argument'. An argument is a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses. In this case the argument 'jesse' was passed to the function 'greet_user()', and the value was assigned to the parameter 'username'.

# NOTE
People sometimes speak of arguments and parameters interchangeably. Don't be surprised if you see the variables in a function definition referred to as arguments or variables in a function call refered to as parameters.