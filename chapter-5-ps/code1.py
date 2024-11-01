'''1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
'''

dictionary = {
    "sooraj": "Sun",
    "chaand": "Moon",
    "paani": "Water",
    "garmi": "Heat",
    "khushi": "Happiness",
    "dukh": "Sorrow",
    "prem": "Love",
    "sapna": "Dream",
    "sangee": "Music",
    "shanti": "Peace"
}

base_word = input("Enter Hindi word from dictionary: ").strip().lower()

if base_word in dictionary:
    print(f"The meaning of {base_word} = {dictionary[base_word]}")
else:
    print("Word not found in dictionary.")
