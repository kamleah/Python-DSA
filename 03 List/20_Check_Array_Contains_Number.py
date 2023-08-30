# Create an array of numbers from 1 to 100
myArray = list(range(1, 101))


# Function to find the index of a number in the array
def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i  # Return the index if the number is found
    return None  # Return None if the number is not found


# Number to find in the array
target = 45

# Call the function to find the index of the target number
index = findNumber(myArray, target)

# Print the index of the target number (if found)
if index is not None:
    print(f"The index of {target} is: {index}")
else:
    print(f"{target} not found in the array")

# Alternatively, use the index() method to find the index of the target number
try:
    index_using_method = myArray.index(target)
    print(f"The index of {target} using index() method is: {index_using_method}")
except ValueError:
    print(f"{target} not found in the array using index() method")
