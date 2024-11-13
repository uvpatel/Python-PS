'''1. Write a python program to display a user entered name followed by Good
Afternoon using input () function'''

try:
    name = str(input("Enter your name: "))

    print(f"Good Afternoon {name}")
except TypeError:
    print("Input should be in string")   
finally:
    print("End of programme")     
