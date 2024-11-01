'''4. Write a python program to print the contents of a directory using the os module.
Search online for the function which does that. '''




import os  # Importing the 'os' module, which provides functions to interact with the operating system

# Specify the directory path
directory_path = "."  # Setting the directory path to the current directory (".") 

# List the contents of the directory
try:
    contents = os.listdir(directory_path)  # Attempting to list all items in the specified directory
    print("Directory Contents:")  # Printing header for directory contents
    for item in contents:  # Looping through each item in the directory
        print(item)  # Printing each item (file/folder) in the directory
except FileNotFoundError:  # Catching the error if the specified directory does not exist
    print(f"The directory {directory_path} was not found.")  # Displaying an error message if directory is not found
