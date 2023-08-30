# Title: Common Pitfalls and How to Avoid Them in List Manipulation

# Example 1: Incorrect use of sort() method
myList = [2, 4, 3, 1, 5, 7]
myList = myList.sort()  # Incorrect: sort() returns None and sorts in-place
print("Example 1:")
print("Incorrect Result (sort() returns None):", myList)  # Prints: None
print()

# Example 2: Correct use of sort() method
myList3 = [2, 4, 3, 1, 5, 7]
myList3.sort()
print("Example 2:")
print("Correct Result after sort():", myList3)  # Prints: [1, 2, 3, 4, 5, 7]
print()

# Example 3: Incorrect use of append() method
myList2 = [2, 4, 3, 1, 5, 7]
myList2.append(10)  # Correctly adds 10 to the end of the list
print("Example 3:")
print("Modified List after append():", myList2)  # Prints: [2, 4, 3, 1, 5, 7, 10]
print()

# Example 4: Correct use of concatenation to add an element
myList4 = [2, 4, 3, 1, 5, 7]
myList4 = myList4 + [10]  # Correctly creates a new list by concatenating
print("Example 4:")
print("Modified List after concatenation:", myList4)  # Prints: [2, 4, 3, 1, 5, 7, 10]
