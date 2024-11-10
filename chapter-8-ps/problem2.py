# 2. Write a python program using function to convert Celsius to Fahrenheit.

def CelsiusToFahrenheit(Celsius):
    print(f"The fahrenheit of given Celsius {Celsius} temp = {(9*Celsius)/5 + 32}")
n = int(input("How many time you want to convert: "))
for i in range(0,n):
    c = float(input("Enter celsius: "))
    CelsiusToFahrenheit(c)    
