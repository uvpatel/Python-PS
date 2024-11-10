# 1. Write a program to find the greatest of four numbers entered by the user.

n1 = float(input("Enter number: "))
n2= float(input("Enter number: "))
n3 = float(input("Enter number: "))
n4 = float(input("Enter number: "))

if(n1 == n2 == n3 == n4):
    print("Enter different number all numbers are same")
else:
    if(n1>n2 and n1 > n3 and n1>n4):
        print(f"Number {n1} is gretest above all number")
    elif(n2>n1 and n2> n3 and n2>n4):
        print(f"Number {n2} is gretest above all number")
    if(n3>n2 and n3> n1 and n3>n4):
        print(f"Number {n3} is gretest above all number")
    if(n4>n2 and n4> n3 and n4>n1):
        print(f"Number {n4} is gretest above all number")
    else:
        if(n1 == n2 and n1 and n2>n3 and n1 and n2>n4):
            print("Number one and two are equal and greatest")
        elif(n3 == n2 and n3 and n2>n1 and  n3 and n2>n4):
            print("Number  three and two are equal and greatest")
        elif(n1 == n4 and n1 and n4>n3 and n1 and n4 >n2):
            print("Number one and  four are equal and greatest")
        elif(n1 == n3 and n1 and n3>n2 and n3 and n1>n4):
            print("Number one and three are equal and greatest")
        
        elif(n2 == n4 and n2 and n4>n1 and n4 and n2>n3):
            print("Number  four and two are equal and greatest")

        elif(n3 == n4 and n3 and n4>n1 and n3 and n4>n2):
            print("Number three and four  are equal and greatest")
        else:
            if( n1 == n2 == n3 and n1 and n2 and n3 > n4):
                print("Number one , two and three are equal and greter than number four")
            elif( n1 == n2 == n4 and n1 and n2 and n4 > n3):
                print("Number one , two and four are equal and greter than number four")
            elif( n4 == n2 == n3 and n4 and n2 and n3 > n1):
                print("Number   four, two and three are equal and greter than number four")
          