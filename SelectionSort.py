# Creates selection sort function
def selection_sort(arr):

    # Loops through every index
    for i in range(len(arr)):

        # Assumes current index is the smallest
        min_index = i

        # Searches remaining elements
        for j in range(i + 1, len(arr)):

            # Checks for smaller value
            if arr[j] < arr[min_index]:

                # Updates smallest index
                min_index = j

        # Swaps smallest value into correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Returns sorted array
    return arr


# Accepts numbers from user
arr = list(map(int, input("Enter numbers: ").split()))

# Displays sorted result
print("Sorted:", selection_sort(arr))