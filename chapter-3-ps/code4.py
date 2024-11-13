# 4. Replace the double space from problem 3 with single spaces.





try:
# User input.
    string = str(input("Enter string: "))

#  how to apply: nameofvariable.replace("from","to")
#  This replace methods of given argument replace double space by single space.
    print(string.replace("  "," "))

except TypeError:
    print("Input should be in forms of string: ")    

finally:
    print("End")
