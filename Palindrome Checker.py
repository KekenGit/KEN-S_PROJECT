# Accepts word or sentence
text = input("Enter a word or sentence: ")

# Removes spaces and converts to lowercase
cleaned = text.replace(" ", "").lower()

# Reverses the text
reversed_text = cleaned[::-1]

# Displays comparison
print("\nOriginal :", cleaned)
print("Reversed :", reversed_text)

# Checks palindrome
if cleaned == reversed_text:
    print("Result   : Palindrome")
else:
    print("Result   : Not Palindrome")