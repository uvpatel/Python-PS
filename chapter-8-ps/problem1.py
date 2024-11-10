# 1. Write a program using functions to find greatest of three numbers.

def greterstNum(a,b,c):
    
    if(a == b == c):
        print("All numbers are same and equal, Enter unique numbers: ")

    elif(a>b and a>c):
        print("First number is gretest")
    elif(b>a and b>c):
        print("Second number is gretest")
    elif(c>b and c>a):
        print("Third number is gretest")
    else:
        if( a == b and a and b>c):
            print("Number one and number two are same and greter than third number")
        elif(a == c and a and c > b):
            print("Number one and third are equal and greter thab second number")
        else:
            print("Number two and three are  equal and greter than one")
n = int(input("Enter how many times you want to use this function: "))
 
for i in range(0,n): 
    fir_num = float(input("Enter number: "))
    second_num = float(input("Enter number: "))
    third_num = float(input("Enter number: "))
    greterstNum(fir_num,second_num,third_num) # put your arguments in parnthisis and seperate it with comma.