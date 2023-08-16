import numpy as np

# Create a 2D array
originalArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)

# Print the original 2D array
print("Original 2D Array:")
print(originalArray)

# Remove the first row from the array
newArrayWithoutFirstRow = np.delete(originalArray, 0, axis=0)

# Print the modified 2D array
print("\nModified 2D Array without the first row:")
print(newArrayWithoutFirstRow)

# Remove the first column from the array
newArrayWithoutFirstColumn = np.delete(originalArray, 0, axis=1)

# Print the modified 2D array
print("\nModified 2D Array without the first column:")
print(newArrayWithoutFirstColumn)
