# Accepts binary input
binary = input("Enter a binary number: ")

# Starts counter
ones = 0
zeros = 0

# Loops through every digit
for digit in binary:

    # Counts ones
    if digit == '1':
        ones += 1

    # Counts zeros
    elif digit == '0':
        zeros += 1

# Displays results
print("\n===== BINARY ANALYSIS =====")
print("Binary Number :", binary)
print("Number of 1s  :", ones)
print("Number of 0s  :", zeros)

# Determines binary type
if ones > zeros:
    print("Analysis      : More ones detected")
elif zeros > ones:
    print("Analysis      : More zeros detected")
else:
    print("Analysis      : Equal number of ones and zeros")