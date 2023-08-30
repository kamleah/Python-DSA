# Slicing to exclude the last element
myList = ["a", "b", "c", "d", "e", "f", "g"]
print(
    "Slicing to Exclude Last Element:", myList[:-1]
)  # Time Complexity: O(n), Space Complexity: O(n)

# Slicing to start from the second element
myList2 = ["a", "b", "c", "d", "e", "f", "g"]
print(
    "Slicing to Start from Second Element:", myList2[1:]
)  # Time Complexity: O(n), Space Complexity: O(n)

# Replacing the first two elements with "x" and "y"
myList3 = ["a", "b", "c", "d", "e", "f", "g"]
myList3[0:2] = ["x", "y"]
print(
    "Replacing First Two Elements:", myList3
)  # Time Complexity: O(k), Space Complexity: O(1), where k is the number of replaced elements

# Removing the last element using pop()
myList4 = ["a", "b", "c", "d", "e", "f", "g"]
myList4.pop()
print(
    "Removing Last Element using pop():", myList4
)  # Time Complexity: O(1), Space Complexity: O(1)

# Removing an element at index 1 using del
myList5 = ["a", "b", "c", "d", "e", "f", "g"]
del myList5[1]
print(
    "Removing Element at Index 1 using del:", myList5
)  # Time Complexity: O(n), Space Complexity: O(n)

# Removing elements from index 1 to 3 using del
myList6 = ["a", "b", "c", "d", "e", "f", "g"]
del myList6[1:4]
print(
    "Removing Elements from Index 1 to 3 using del:", myList6
)  # Time Complexity: O(n), Space Complexity: O(n)

# Removing element "d" using remove()
myList7 = ["a", "b", "c", "d", "e", "f", "g"]
myList7.remove("d")
print(
    "Removing Element 'd' using remove():", myList7
)  # Time Complexity: O(n), Space Complexity: O(n)
