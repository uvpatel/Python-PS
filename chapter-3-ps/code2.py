# 2. Write a program to fill in a letter template given below with name and date.

# Template letter with placeholders for name and date

letter = '''Dear <|Name|>,
You are selected!
<|date|>'''

# Taking user input for name and date
Name = input("Enter your name: ")
date = input("Enter the date: ")

# Replacing placeholders with user inputs
letter = letter.replace("<|Name|>", Name)  # Replacing <|Name|> with the user's name
letter = letter.replace("<|date|>", date)  # Replacing <|date|> with the user's provided date

# Printing the final letter with the replacements
print(letter)


