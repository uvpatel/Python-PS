''' 2. Write a program to input eight numbers from the user and display all the unique
numbers (once). '''

def get_unique_numbers():
    numbers = []

    # Input 8 numbers from the user
    for i in range(8):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Get unique numbers using a set
    unique_numbers = set(numbers)

    # Display the unique numbers
    print("Unique numbers are:", unique_numbers)

# Call the function
get_unique_numbers()
