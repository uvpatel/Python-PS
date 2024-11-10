''' 6. Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => A
80 – 90 => B
70 – 80 => C
60 – 70 =>D
50 – 60 => E
<50 => F'''

marks_phy = float(input("Enter marks of physics: "))
marks_math = float(input("Enter marks of maths: "))
marks_chem = float(input("Enter marks of chemistry : "))

persentage = (marks_chem+marks_math+marks_phy)/3

print(f"Your persentage are {persentage}")

if(100>=persentage>90):
    print("Your gread is A")
elif(80<persentage<=90):
    print("Your gread is B")
elif(70<persentage<=80):
    print("Your gread is C")
elif(60<persentage<=70):
    print("Your gread is D")
elif(50<persentage<=60):
    print("Your gread is E")
elif(40<persentage<=50):
    print("Your gread is F")
else:
    print("You are fail")