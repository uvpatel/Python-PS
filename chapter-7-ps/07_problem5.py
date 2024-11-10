# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter number: "))

sum = 0

for i in range(0,n+1):
    sum = sum + i
print(f"The sum of {n} number is {sum}")    