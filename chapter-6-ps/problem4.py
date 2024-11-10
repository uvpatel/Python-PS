'''4. Write a program to find whether a given username contains less than 10
characters or not.'''

userName = input("Enter your name: ")

if(len(userName)<10):
    print("The given name is contain 10 or less than characters")
else:
    print("The given name is contain more than 10 characters")    