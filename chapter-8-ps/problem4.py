# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sumofn(n):
    print(f"The sum of {n} is {sum}")

    if(n==0):
        return 0
    else:
        return n + sumofn(n-1)

m = int(input("Enter number how many times you want to use this function"))    
for i in range(0,m):

    n = int(input("Enter number: "))
    sumofn(n)
    

    
