# Insertion in Two Dimensional Array

import numpy as np

# Create a 2D array
originalArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)

# Print the original 2D array
print("Original 2D Array:")
print(originalArray)

# Insert a new column at the beginning of the array
newArrayWithAddedColumn = np.insert(
    originalArray, 0, [[1, 2, 3, 4]], axis=1
)  # Insert a new column at axis 1 (column-wise)
print("\nNew Array with Added Column:")
print(newArrayWithAddedColumn)

# Insert a new row at the beginning of the array
newArrayWithAddedRow = np.insert(
    originalArray, 0, [[1, 2, 3, 4]], axis=0
)  # Insert a new row at axis 0 (row-wise)
print("\nNew Array with Added Row:")
print(newArrayWithAddedRow)
