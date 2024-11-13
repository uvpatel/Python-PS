# 2. Write a python program to find remainder when a number is divided by z


# Enter numartor

try: 
    numarator = int(input("Enter numarator: "))
    denominator = int(input("Enter number: "))

    remender = numarator%denominator
    if(remender==0):
        print("The given number is divisible")

    else:
        print("The given number is not divisible")
except ValueError:
    print("Numarator Can't divisivble by zero")        
except NotImplemented:
    print("Input should be integer")        

