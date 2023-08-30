# Working with Tuples
# Accessing tuple elememts
# Creating a tuple with multiple elements
newtuple = ("a", "b", "c", "d", "e", "f")

# Accessing elements of the tuple
first_element = newtuple[0]  # Accessing the first element ("a")
last_element = newtuple[-1]  # Accessing the last element ("f")
sliced_elements = newtuple[1:3]  # Slicing elements from index 1 to 2 ("b" and "c")

# Printing the accessed elements
print("First Element:", first_element)  # Output: a
print("Last Element:", last_element)  # Output: f
print("Sliced Elements:", sliced_elements)  # Output: ('b', 'c')

# Attempting to modify a tuple (will result in an error)
try:
    newtuple[0] = "z"  # Trying to modify the first element (will raise an error)
except Exception as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment
