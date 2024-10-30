#Module3Lesson5
Assignment 

Explanation of the Code:
Imports the os module: This is necessary for interacting with the operating system and handling directory operations.

Defines the list_directory_contents function:

It takes a path as an argument.
Uses os.scandir() to iterate through the contents of the directory.
Catches exceptions such as FileNotFoundError and PermissionError to handle invalid or inaccessible directories.
Checks if the script is run as the main program:

Prompts the user for the directory path.
Calls the list_directory_contents function with the provided path.
Expected Outcome:
When you run the script, it will prompt you for a directory path. After entering a valid path, it will list all files and subdirectories within that directory. If the path is invalid or inaccessible, it will display an appropriate error message.
