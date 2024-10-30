# with comments


import os  # Import the os module to interact with the operating system

# Specify the directory path
directory_path = "."  # "." refers to the current working directory

# List the contents of the directory
try:
    # os.listdir() returns a list of files and directories in the specified path
    contents = os.listdir(directory_path)
    
    # Print the contents of the directory
    print("Directory Contents:")
    for item in contents:
        print(item)  # Print each item (file or sub-directory) in the directory
except FileNotFoundError:
    # Handle the case where the directory is not found
    print(f"The directory {directory_path} was not found.")
