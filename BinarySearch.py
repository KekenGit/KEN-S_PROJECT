# Creates a function for binary search
def binary_search(arr, target):

    # Starting index
    left = 0

    # Last index
    right = len(arr) - 1

    # Repeats while search area is valid
    while left <= right:

        # Gets middle index
        mid = (left + right) // 2

        # Checks if middle value equals target
        if arr[mid] == target:

            # Returns middle index
            return mid

        # Checks if target is larger
        elif arr[mid] < target:

            # Searches right half
            left = mid + 1

        # Executes if target is smaller
        else:

            # Searches left half
            right = mid - 1

    # Returns -1 if not found
    return -1


# Accepts sorted numbers
arr = list(map(int, input("Enter sorted numbers: ").split()))

# Accepts target number
target = int(input("Enter number to search: "))

# Displays the returned index
print("Index:", binary_search(arr, target))