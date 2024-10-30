'''4. Write a python program to print the contents of a directory using the os module.
Search online for the function which does that. '''




import os

# Specify the directory path
directory_path = "."

# List the contents of the directory
try:
    contents = os.listdir(directory_path)
    print("Directory Contents:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_path} was not found.")
