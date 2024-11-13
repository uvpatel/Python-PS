# 1. Write a python program to add two numbers.


#  Take input from user 

try:
    a = float(input("Enter first number: "))
    b= float(input("Enter second number: "))
    print("The sum of two given number is: ",a+b)

except ValueError:
    print("Input should in float or integer")

finally:
    print("End of programme")
