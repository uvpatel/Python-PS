
#Taking input from users.

try:
    in_put = input("Enter your input: ")
# type function print type of given input.
    print("The type of input is: ",type(in_put))

except TypeError:
    if(in_put == None):
     print("Input is not given")   
