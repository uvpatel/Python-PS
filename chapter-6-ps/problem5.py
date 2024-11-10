# 5. Write a program which finds out whether a given name is present in a list or not.

list = ["Darshan" , "Heer" , "Krish","Hiten","Parth"]

name = input("Enter name: ")
if(name in list):
    print("The given name is in list")
else:
    print("The given name isn't in list")