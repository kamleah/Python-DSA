# Tuple vs List: Differences and Common Operations

# Lists are mutable, tuples are immutable
# Common functions for both: len(), max(), min(), sum(), any(), all(), sorted()
# Methods exclusive to lists: append(), insert(), remove(), pop(), clear(), sort(), reverse()

# Working with Lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original List:", list1)

list1[2] = 10  # Modifying an element in the list
print("Modified List:", list1)

list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19]  # Reassigning the list
print("Reassigned List:", list1)

# Working with Tuples and Lists
newList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newTuple = 1, 2, 3, 4, 5, 6, 7, 8, 9
print("New List:", newList)
print("New Tuple:", newTuple)

try:
    newTuple[1] = 20  # Attempting to modify a tuple (will raise an error)
except Exception as e:
    print("Error:", e)

newList[0] = 10  # Modifying a list element
print("Modified List:", newList)

newTuple = 1, 2, 3, 4  # Reassigning the tuple
print("Reassigned Tuple:", newTuple)

try:
    del newTuple[0]  # Attempting to delete an element from tuple (will raise an error)
except Exception as e:
    print("Error:", e)

print("Remaining List:", newList)
del newList[0]  # Deleting an element from list
print("List after Deletion:", newList)

# Sorting Lists and Tuples
list2 = [(1, 2), (9, 0), (8, 7)]
tuple2 = ((1, 3), (0, 9), (6, 7))
print("List of Tuples:", list2)
print("Tuple of Tuples:", tuple2)


# Explanation:
# - This code illustrates the differences between lists and tuples and showcases common operations.
# - Lists are mutable, allowing elements to be modified, added, and removed.
# - Tuples are immutable, preventing element modifications.
# - The `del` keyword is used to delete elements from lists, but not from tuples.
# - Tuples can contain lists and vice versa.
# - Sorting can be applied to both lists of tuples and tuples of tuples.
# - Each operation is explained with comments for clarity.
