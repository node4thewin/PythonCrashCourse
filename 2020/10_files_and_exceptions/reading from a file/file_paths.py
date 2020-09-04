# File Paths

# When you pass a simple filename like 'pi_digits.py' to the open() function, Python looks in the directory where the file that's currently being executed (that is, your .py program file) is stored.

# Sometimes, depending on how you organize your work, the file you want to open won't be in the same directory as you program file. For example, you might store your program files in a folder called 'python_work'; inside 'python_work', you might have another folder called 'text_files' to distinguish your program files from the text file they're manipulating. Even though 'text_files' is in 'python_work', just passing open() in 'python_work' and stop there; it won't go on and look in text_files. To get Python to open files from a directory other than the one where your program file is stored, you need to provide a 'file path', which tells Python to look in a specific location relative to the directory where the currently running program file is stored. For example, you'd write:

# with open('text_files/filename.txt') as file_object:

# This line tells Python to look for the desired .txt file in the folder 'text_files' and assumes that 'text_files' is located inside 'python_work' (which it is).

# NOTE - Windows systems use a backslach (\) instead of a forward slash (/) when displaying file paths, but you can still use forward slashes in your code.

# You can also tell Python exactly where the file is in your computer regardsless of where the program that's being executed is stored. This is called an 'absolute file path'. You use an absolute file path if a relative path doesn't work. For instnace, if you've put 'text_files' in some folder other than 'python_work'--say, a folder called 'other_files'--then just passing 'open()' the path 'text_files/filename.txt' won't work because Python will only look for that location inside 'python_work'. You'll need to write out a full path to clarify where you want Python to look.

# Absolute paths are usually longer than relative paths, so it's helpful to assign them to a variable an dthen pass that variable 'open()':

# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'

# with open(file_path) as file_object:

# Using absolute paths, you can read files from any location on your system. Fo rnow it's easiest to store files in the same directory as your program files or in a folder such as 'text_files' within the directory that stores your program files.

# NOTE - If you try to use backslashes in a file path, you'll get an error because the backslash is used to escape characters in strings. For example, in the path "C:\path\to\file.txt", the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape each one in the path, like this: C:\\path\\to\\file.txt".