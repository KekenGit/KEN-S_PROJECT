# Accepts numbers from user
arr = list(map(int, input("Enter numbers: ").split()))

# Creates empty list for even numbers
even_numbers = []

# Loops through every number
for num in arr:

    # Checks if number is even
    if num % 2 == 0:

        # Adds even number to the list
        even_numbers.append(num)

# Checks if there are even numbers
if len(even_numbers) > 0:

    # Calculates average
    mean = sum(even_numbers) / len(even_numbers)

    # Displays result
    print("Mean of even numbers:", mean)

# Executes if no even numbers exist
else:

    # Displays message
    print("No even numbers found")