# 2. Write a program to fill in a letter template given below with name and date.

# Template letter with placeholders for name and date

letter = '''Dear <|Name|>,
You are selected!
<|date|>'''
try:
    letter = '''
        Dear Name,
        You are selected!
        <|Date|>'''

# Taking user input for name and date
    name = str(input("Enter name: "))
    date = int(input("Enter date: "))
  # Replacing placeholders with user inputs
  # Replacing <|Name|> with the user's name
  # Replacing <|date|> with the user's provided date
  # Printing the final letter with the replacements
    print(letter.replace("Name",name) and letter.replace("<|Date|>",date))

except TypeError:
    print("Fill input properly")



