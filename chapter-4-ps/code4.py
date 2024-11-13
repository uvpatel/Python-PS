# 4. Write a program to sum a list with 4 numbers
try:
    number = [] #Empty list

# Taking input from user:
    a = float(input("Enter number: "))
    number.append(a)
    c = float(input("Enter number: "))
    number.append(c)
    b = float(input("Enter number: "))
    number.append(b)
    d = float(input("Enter number: "))
    number.append(d)

# Printing sum of list elements using sum fucuntion.
    print("The sum of list elements: ",sum(number))
except TypeError:
    print("Input should be in number")   

finally:
  print("End")
