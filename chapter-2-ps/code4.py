'''4. Use comparison operator to find out whether ‘a’ given variable a is greater than
‘b’ or not.'''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

#  if - else ladder.
if(a == b):
    print("The given numbers are same")
    
else:
    if(a>b):
        print("First number is greater than second number")
    
    else:
        print("Second number is greater than first number")
