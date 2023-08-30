# Title: Arrays vs Lists in Python

# Similarities
# ============
# 1. Both data structures are mutable.
# 2. Both can be indexed and iterated through.
# 3. They can be both sliced.

# Differences
# ============
# 1. The main difference between arrays and lists is the operations you can perform on them.
#    Arrays are specially optimized for arithmetic operations.
# 2. Data types can be mixed in lists, but arrays usually contain elements of the same type.

import numpy as np

# Example for difference 1: Arithmetic Operations
print("Example for Difference 1 (Arithmetic Operations):")
myArray1 = np.array([1, 2, 3, 4, 5, 6, 7])
myList1 = [1, 2, 3, 4, 5, 6, 7]

try:
    array_result = myArray1 / 2
    print("Array Division Result:", array_result)
except TypeError:
    print("Error: Cannot perform division on the array")
print()

try:
    list_result = myList1 / 2
    print("List Division Result:", list_result)
except TypeError:
    print("Error: Cannot perform division on the list")
print()

try:
    list_result = [x / 2 for x in myList1]
    print("List Division Result:", list_result)
except TypeError:
    print("Error: Cannot perform division on the list")
print()

# Example for Difference 2: Data Types
print("Example for Difference 2 (Data Types):")
myArray2 = np.array([1, 2, 3, 4, 5, 6, 7, "a"])  # Mixed data types including a string
myList2 = [1, 2, 3, 4, 5, 6, 7, "a"]

try:
    array_result = myArray2 / 2
    print("Array Division Result:", array_result)
except TypeError:
    print("Error: Cannot perform division on the array")

try:
    list_result = [x / 2 for x in myList2]
    print("List Division Result:", list_result)
except TypeError:
    print("Error: Cannot perform division on the list")
print()
# Note: The myList2 has mixed data types including a string, which is not ideal for mathematical operations.
