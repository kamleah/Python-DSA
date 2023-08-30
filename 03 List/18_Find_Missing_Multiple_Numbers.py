# Create a list containing numbers from 1 to 100
all_numbers = list(range(1, 101))

# Simulate missing numbers by removing 20 and 50
missing_number_1 = 20
missing_number_2 = 50
all_numbers.remove(missing_number_1)
all_numbers.remove(missing_number_2)

# Create a fresh list containing numbers from 1 to 100 again
all_numbers2 = list(range(1, 101))

# Find the missing numbers by comparing the two lists
missing_numbers = [number for number in all_numbers2 if number not in all_numbers]

# Print the original list with missing numbers
print("Original list with missing numbers:", all_numbers2)

# Print the simulated missing numbers
print("Simulated missing numbers:", [missing_number_1, missing_number_2])

# Print the actual missing numbers
print("Actual missing numbers:", missing_numbers)
