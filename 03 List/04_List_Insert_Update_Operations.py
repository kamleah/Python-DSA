#  update or insert - list

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Printing the initial list
print("Initial List:", myList)  # Time Complexity: O(n), Space Complexity: O(n)

# Inserting 12 at the beginning of the list
myList.insert(0, 12)
print(
    "After Inserting 12 at the Beginning:", myList
)  # Time Complexity: O(n), Space Complexity: O(n)

# Appending 12 to the end of the list
myList.append(12)
print(
    "After Appending 12 at the End:", myList
)  # Time Complexity: O(1), Space Complexity: O(1)
