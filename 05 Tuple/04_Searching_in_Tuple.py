# Searching Through a Tuple

# Creating a tuple with multiple elements
newTuple = ("a", "b", "c", "d", "e", "f")

# Using 'in' operator to search for elements in the tuple
print("Is 'b' in the tuple?", "b" in newTuple)  # Output: True
print("Is 'i' in the tuple?", "i" in newTuple)  # Output: False


# Function to search for an element in the tuple and return its index
def searchTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)  # Return the index of the found element
    return "The element does not exist"  # Return this message if element is not found


# Using the searchTuple function to find the index of an element in the tuple
element_to_search = "d"
result = searchTuple(newTuple, element_to_search)
print(
    f"The index of '{element_to_search}' in the tuple is:", result
)  # Output: The index of 'd' in the tuple is: 3
