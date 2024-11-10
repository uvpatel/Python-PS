'''2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''

marks_phy = float(input("Enter marks of physics: "))
marks_math = float(input("Enter marks of maths: "))
marks_chem = float(input("Enter marks of chemistry : "))

persentage = (marks_chem+marks_math+marks_phy)/3

print(f"Your persentage are {persentage}")

if(persentage<40):
    print("You are fail, better luck next time")
else:
    if(marks_math <33):
        print("You are fail in Maths")
        print(f"Maths marks = {marks_math}")
    elif(marks_chem<33):
        print("You are fail in Chemestry")
        print(f"Chemistry marks = {marks_chem}")
    elif(marks_phy<33):
        print("You are fail in Physics")
        print(f"Physics marks = {marks_phy}")
    else:
        if(marks_phy and marks_chem < 33):
            print("You are fail in physics and chemestry")
            print(f"Phy = {marks_phy} and chem = {marks_chem}")
        elif(marks_chem and marks_math < 33):
            print("You are fail in Chemestry and Maths")
            print(f"Maths mark = {marks_math} and chem = {marks_chem}")
        elif(marks_phy and marks_math < 33):
            print("You are fail in Physics and Maths")
            print(f"Phy = {marks_phy} and Maths marks = {marks_math}")
        elif(marks_phy and marks_math and marks_chem < 33):
            print("You are fail in all subject")
