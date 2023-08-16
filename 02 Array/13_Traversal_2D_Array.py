import numpy as np

# Create a 2D array
twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)

# Print the original 2D array
print("Original 2D Array:")
print(twoDArray)


# Function to traverse elements in a 2D array
def traverse2DArray(array):
    """
    Traverses a 2D array and prints each element.

    :param array: The 2D array to be traversed.
    """
    for row in range(len(array)):  # Loop through rows (m rows)
        for col in range(len(array[0])):  # Loop through columns (n columns)
            element = array[row][col]  # Accessing element at row 'row', column 'col'
            print(f"Element at row {row}, column {col}: {element}")


# Call the function to traverse and print the elements
print("\nTraversing 2D Array:")
traverse2DArray(twoDArray)

# Explanation statement
print(
    "\nTime Complexity: O(mn) - where 'm' is the number of rows and 'n' is the number of columns."
)
print("Space Complexity: O(1) - constant space is used.")
