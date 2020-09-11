# Functions
In this chapter you'll learn to write 'functions', which are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you've defined in a function, you call the function responsible for it. If you need to perform that task multiple times throughout your program, you don't need to type all the code for the same task again and again; you just call the function dedicated to handling the task, and the call tells Python to run the code inside the function. You'll find that using functions makes your programs easier to write, read, test, and fix.

In this chapter you'll also learn ways to pass information to functions. You'll learn how to write certain functions whose primary job is to display information and other functions designed to process data and return a value or set of values. Finally, you'll learn how to store functions in separate files called 'modules' to help organize your main program files.

# Arguments and Parameters

In 'passing_information_to functions.py' we used the 'greet_user()' function, and defined 'greet_user()' to require a value for the variable 'username'. Once we called the function and gave it the information (a person's name), it printed the right greeting.

The variable 'username' in the definition of 'greet_user()' is an example of a 'parameter', a piece of information the function needs to do its job. The value 'jesse' in 'greet_user('jesse') is an example of an 'argument'. An argument is a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses. In this case the argument 'jesse' was passed to the function 'greet_user()', and the value was assigned to the parameter 'username'.

# NOTE
People sometimes speak of arguments and parameters interchangeably. Don't be surprised if you see the variables in a function definition referred to as arguments or variables in a function call refered to as parameters.

# Summary

In this chapter you learned how to write functions and to pass arguments so that your functions have access to the information they need to do their work. You learned how to use positional and keyword arguments, and how to accept an arbitrary number of arguments. You saw functions that display output and functions that return values. You learned how to use functions with lists, dictionaries, if statements, and while loops. You also saw how to store your functions in separate files called modules, so your program files will be simpler and easier to understand. Finally, you learned to style your functions so your programs will continue to be well-structured and as easy as possible for you and others to read.

One of your goals as a programmer should be to write simple code that does what you want it to, and functions help you do this. They allow you to write blocks of code and leave them alone once you know they work. When you know a function does its job correctly, you can trust that it will continue to work and move on to your next coding task.
Functions allow you to write code once and then reuse that code as many times as you want. When you need to run the code in a function, all you need to do is write a one-line call and the function does its job. When you need to modify a function’s behavior, you only have to modify one block of code, and your change takes effect everywhere you’ve made a call to that function.
Using functions makes your programs easier to read, and good func- tion names summarize what each part of a program does. Reading a series of function calls gives you a much quicker sense of what a program does than reading a long series of code blocks.

Functions also make your code easier to test and debug. When the bulk of your program’s work is done by a set of functions, each of which has a specific job, it’s much easier to test and maintain the code you’ve written. You can write a separate program that calls each function and tests whether each function works in all the situations it may encounter. When you do this, you can be confident that your functions will work properly each time you call them.

In Chapter 9 you’ll learn to write classes. Classes combine functions and data into one neat package that can be used in flexible and efficient ways.

# Solutions to "Try It Yourself":
https://ehmatthes.github.io/pcc_2e/solutions/solutions/
