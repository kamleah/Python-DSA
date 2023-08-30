# Traversing Through a Tuple

# Creating a tuple with multiple elements
newTuple = ("a", "b", "c", "d", "e", "f")

# Using a for loop to traverse through the tuple elements
print("Using for loop:")
for element in newTuple:
    print(element)  # Output: a, b, c, d, e, f

# Using a for loop and range to traverse through the tuple using indexing
print("\nUsing for loop with indexing:")
for i in range(len(newTuple)):
    print(newTuple[i])  # Output: a, b, c, d, e, f
