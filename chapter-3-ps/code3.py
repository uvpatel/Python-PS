# 3. Write a program to detect double space in a string.

try:
    string = input("Enter string: ")

# This count methods count given argument double spaces.
    print(f"The double spaces are present in this string is:{string.count("  ")}")

except ValueError:
    print("No double space detected in this input")    
except TypeError:
  print("Output should be in integer")


