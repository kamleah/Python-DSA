# Two Dimensional Array
# An array with a buch of values have been declared with double index
# a[i][j] -> i and j between 0 and n

import numpy as np

# Create a 2D array
twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)


# Function to access elements in a 2D array
def accessElement(array, row_index, col_index):
    """
    Accesses an element in a 2D array using specified row and column indices.

    :param array: The 2D array to access elements from.
    :param row_index: The index of the desired row.
    :param col_index: The index of the desired column.
    """
    # Check if the provided indices are within the valid range
    if row_index >= len(array) or col_index >= len(array[0]):
        print("Invalid Indices")
    else:
        element = array[row_index][col_index]
        print(f"Element at row {row_index}, column {col_index}: {element}")


# Print the original 2D array
print("Original 2D Array:")
print(twoDArray)

# Call the function to access a specific element
accessElement(twoDArray, 1, 2)  # Replace indices with the ones you want to access
