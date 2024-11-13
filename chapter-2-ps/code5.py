# 5. Write a python program to find an average of two numbers entered by the user.


try:
# Taking input from users.
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter  second number: "))

    avg = (number_1+number_2)/2
# Printing output.
    print("The avrage of given number is: ",avg)

except ValueError:
    print("Input should be float or integer")    

finally:
    print("End")
