# Insert a value iin array

from array import *

arr1 = array("i", [1, 2, 3, 4, 5])
arr2 = array("d", [1.2, 2.3, 3.4, 4.5, 5.6])

print("Before Insert Array")
print(arr1)
print(arr2)

arr1.insert(5, 6)
# Time Commplexity for Inserting at the end of the array is O(1)
# Because we don't have to move an array element, it is not ttaking to much of time.
# Inserting an element in end is very fast.

arr1.insert(2, 5)
#  Time Commplexity for Inserting in between full array is O(n)
# Inserting an element in middle it's too time taking because we have to mmove one element in right.

print("After Insert Array")
print(arr1)

print("Add a value a position 0")
arr1.insert(0, 0)
print(arr1)
