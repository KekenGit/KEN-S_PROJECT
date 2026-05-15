# Accepts how many temperature readings to enter
count = int(input("How many Celsius readings? "))

# Creates an empty list
temperatures = []

# Loops based on user input
for i in range(count):

    # Accepts each temperature
    temp = float(input(f"Enter reading #{i + 1}: "))

    # Adds temperature to the list
    temperatures.append(temp)

# Calculates average
average = sum(temperatures) / len(temperatures)

# Displays all readings
print("\nTemperature Readings:", temperatures)

# Displays the average
print("Average Celsius Reading:", round(average, 2))

# Checks temperature condition
if average >= 35:
    print("Weather Status: Very Hot")
elif average >= 25:
    print("Weather Status: Warm")
else:
    print("Weather Status: Cold")
