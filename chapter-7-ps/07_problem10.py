# 10. Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter number: "))


i = 10
while(i>0):
    print(f"{n}X{i}={n*i}")
    i = i - 1