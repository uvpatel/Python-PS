# 6. Write a python function which converts inches to cms.

def CmToinch(cms):

    print(f"Inches of given cms is { 0.394*cms}")

n = int(input("How many time you want to convert: "))
for i in range(0,n):

    centimeter = float(input("Enter centemeter: "))
    CmToinch(centimeter)

