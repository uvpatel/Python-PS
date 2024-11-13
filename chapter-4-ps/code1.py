# 1. Write a program to store seven fruits in a list entered by the user.

try:
    fruits = []

    f1 = str(input("Enter fruit name: "))
    fruits.append(f1)
    f2 = str(input("Enter fruit name: "))
    fruits.append(f2)
    f3 = str(input("Enter fruit name: "))
    fruits.append(f3)
    f4 = str(input("Enter fruit name: "))
    fruits.append(f4)
    f5 = str(input("Enter fruit name: "))
    fruits.append(f5)
    f6 = str(input("Enter fruit name: "))
    fruits.append(f6)
    f7 = str(input("Enter fruit name: "))
    fruits.append(f7)

    print(fruits)

except TypeError:
    print("Input should be in string")

finally:
     print("End")
