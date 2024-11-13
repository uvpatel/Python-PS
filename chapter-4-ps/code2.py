# This problem same as code 1 

try:

    marks = []

    marks_1 = float(input("Enter marks: "))
    marks.append(marks_1)
    marks_2 = float(input("Enter marks: "))
    marks.append(marks_2)
    marks_3 = float(input("Enter marks: "))
    marks.append(marks_3)
    marks_4 = float(input("Enter marks: "))
    marks.append(marks_4)
    marks_5 = float(input("Enter marks: "))
    marks.append(marks_5)
    marks_6 = float(input("Enter marks: "))
    marks.append(marks_6)
  # this sort method sort list items in ascending order.
    marks.sort

    print(marks)
except ValueError:
    print("Input should be in number")    

# sort() modifies the list directly.(defualt = ascending)
# sorted() creates a new sorted list.
# To sort in descending order, set reverse=True.


# for Descending 
# Descending order
# sorted_numbers_desc = sorted(numbers, reverse=True)
# print("Descending:", sorted_numbers_desc)
