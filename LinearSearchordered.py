# Creates a function for linear search
def linear_search(arr, target):

    # Loops through each index in the array
    for i in range(len(arr)):

        # Checks if current value equals the target
        if arr[i] == target:

            # Returns the index if found
            return i

        # Stops searching early because array is ordered
        elif arr[i] > target:
            break

    # Returns -1 if target is not found
    return -1


# Accepts sorted numbers from the user
arr = list(map(int, input("Enter sorted numbers: ").split()))

# Accepts the target number
target = int(input("Enter number to search: "))

# Calls the function and stores the result
result = linear_search(arr, target)

# Checks if target was found
if result != -1:

    # Displays the index location
    print("Found at index:", result)

# Executes if target is not found
else:

    # Displays not found message
    print("Not found")