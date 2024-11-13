# 6. Write a python program to calculate the square of a number entered by the user.

try:
    number = float(input("Enter number: "))

    print(f"The squre of {number} is: {number**2}")
    
except TypeError:
    print("Input should integer or floating point number")    

finally:
    print("End")    
