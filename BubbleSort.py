# Creates bubble sort function
def bubble_sort(arr):

    # Gets total number of elements
    n = len(arr)

    # Outer loop controls passes
    for i in range(n):

        # Inner loop compares adjacent values
        for j in range(n - i - 1):

            # Checks if left value is bigger
            if arr[j] > arr[j + 1]:

                # Swaps the values
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Returns sorted array
    return arr


# Accepts numbers from user
arr = list(map(int, input("Enter numbers: ").split()))

# Displays sorted result
print("Sorted:", bubble_sort(arr))