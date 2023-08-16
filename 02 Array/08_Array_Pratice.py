from array import *

# 01. Create an array and traverse

traverse_array = array("i", [1, 2, 3, 4, 5, 6, 7])
print("----------------------Traverse an array---------------------")
print(f"Array values are {traverse_array}")
for index, value in enumerate(traverse_array):
    print(f"index [{index}] has value: {value}")


# 02. Access individual elements through indexes
print("\n-----------Access individual elements through indexes-------")
accessing_individual_elements = array("i", [1, 2, 3, 4, 5, 6, 7])
print(f"Array values are {accessing_individual_elements}")
access_index = 5
print(
    f"index [{access_index}] has value: {accessing_individual_elements[access_index]}"
)


# 03.Append any Value to the array using append() method
print("\n-----Append any Value to the array using append() method----")
append_array = array("i", [1, 2, 3, 4, 5, 6, 7])
print(f"Array values before append {append_array}")
append_value = 8
append_array.append(append_value)
print(f"array after append value {append_value} is {append_array}")

# 04. Insert value in a array using insert() method
print("\n--------Insert value in a array using insert() method-------")
insert_array = array("i", [1, 2, 3, 4, 5, 6, 7])
print(f"Array values before insert {insert_array}")
insert_array.insert(3, 11)
print(f"Array values after insert {insert_array}")

# 05. Extend python array using extend() method
print("\n----------Extend python array using extend() method--------")
extent_array1 = array("i", [1, 2, 3, 4, 5, 6, 7])
extent_array2 = array("i", [8, 9, 10, 11, 12, 13, 14])

print("Original Arrays:")
print(f"Array 1: {extent_array1}")
print(f"Array 2: {extent_array2}")

print("\nExtending Array 2 with Array 1:")
extent_array2.extend(extent_array1)
print(f"Extended Array 2: {extent_array2}")

print("\nExtending Array 1 with Extended Array 2:")
extent_array1.extend(extent_array2)
print(f"Extended Array 1: {extent_array1}")

# 06. Add Items from list into array using fromlist() method
print("\n---Add Items from list into array using fromlist() method---")
from_array = array("i", [1, 2, 3, 4, 5, 6, 7])
tempList = [8, 9, 10, 11, 12, 13, 14]

print("\n---Add Items from list into array using fromlist() method---")
print(f"Original array value: {from_array}")
print(f"Temp list value: {tempList}")

from_array.fromlist(tempList)
print(f"Array after adding items from temp list: {from_array}")

# 07. Remove any array element using remove() method
remove_from_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Array:")
print(remove_from_array)

# Remove an element from the array
element_to_remove = 7
remove_from_array.remove(element_to_remove)

print("\nArray after removing element:")
print(remove_from_array)

# 09. Remove last array elements using pop() method
print("\n---Remove last array elements using pop() method---")
pop_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Array:")
print(pop_array)

# Remove the last element from the array using pop()
removed_element = pop_array.pop()

print("\nArray after removing the last element:")
print(pop_array)
print(f"Removed element: {removed_element}")

# 09. Fetch any element through its index usinng index() method
print("\n-----Fetch any element through its index usinng index() method-----")
index_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Array:")
print(index_array)

value_to_find = 4

try:
    index_of_value = index_array.index(value_to_find)
    print(f"\nValue {value_to_find} is found at index: {index_of_value}")
except ValueError:
    print(f"\nValue {value_to_find} is not found in the array.")

# 10. Reverse a python array using reverse() method
print("\n-----Reverse a python array using reverse() method-----")
reverse_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Array:")
print(reverse_array)

reverse_array.reverse()

print("\nArray after reversing:")
print(reverse_array)

# 11. Get array buffer info through buffer_info() method
print("\n----Get array buffer info through buffer_info() method----")
buffer_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Array:")
print(buffer_array)

buffer_info = buffer_array.buffer_info()

print(f"\nBuffer Information: {buffer_info}")
print(f"Address of the buffer: {buffer_info[0]}")
print(f"Size of the buffer: {buffer_info[1]}")

# 12. Check the number of occurance of an element using count() method
print("\n----Check the number of occurance of an element using count() method----")
occurance_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Array:")
print(occurance_array)

value_to_append = 7
occurance_array.append(value_to_append)

count_of_value = occurance_array.count(value_to_append)

print("\nCount of value", value_to_append, "in the array:", count_of_value)
print("Array after appending value:")
print(occurance_array)

# 13. Convert array to string using tostring() method
print("\n----Convert array to string using tostring() method----")
int_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Integer Array:")
print(int_array)

byte_string = int_array.tobytes()

print("\nByte String Representation:")
print(byte_string)

new_array = array("i")
new_array.frombytes(byte_string)

print("\nNew Integer Array created from Byte String:")
print(new_array)

# 14. Convert array to a python list with same elements using tolist() methods
print(
    "\n--------Convert array to a python list with same elements using tolist() methods---------"
)
int_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Integer Array:")
print(int_array)

# Convert the array to a list using tolist()
int_list = int_array.tolist()

print("\nArray converted to a List:")
print(int_list)

# 15. Slice elements from an array
print("\n------Slice elements from an array-------")
int_array = array("i", [1, 2, 3, 4, 5, 6, 7])

print("Original Integer Array:")
print(int_array)

# Slice the array to get a subarray
sliced_subarray = int_array[1:4]

print("\nSlice of the Array (1:4):")
print(sliced_subarray)

# Slice the array to get a subarray starting from index 1 to the end
sliced_subarray2 = int_array[1:]
print("\nSlice of the Array (1:):")
print(sliced_subarray2)

# Slice the array to get a subarray from the beginning to index 3
sliced_subarray3 = int_array[:4]
print("\nSlice of the Array (:4):")
print(sliced_subarray3)

# Slice the entire array to create a copy
sliced_subarray4 = int_array[:]
print("\nCopy of the Array:")
print(sliced_subarray4)
