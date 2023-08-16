import numpy as np

# Create a 2D array
originalArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)

# Print the original 2D array
print("Original 2D Array:")
print(originalArray)


def search_2d_array(array, target):
    """
    Searches for a target value in a 2D array and returns its index if found.

    :param array: The 2D array to search in.
    :param target: The value to search for.
    :return: A message indicating the index where the target value is located or "Element not found".
    """
    for row_index, row in enumerate(array):  # O(mn) time complexity
        for col_index, value in enumerate(row):  # O(n) time complexity
            if value == target:  # O(1) time complexity
                return (
                    f"The value {target} is located at index {row_index}, {col_index}"
                )
    return "Element not found"


# Call the function to search for a value
search_value = 15  # Change this value to search for a different element
result = search_2d_array(originalArray, search_value)
print(result)

# Statement: The code searches for a target value in the 2D array and returns its index if found, demonstrating
# the time complexity of O(m * n) due to nested loops iterating through the rows and columns.
