from array import *

arr1 = array("i", [1, 2, 3, 4, 5])
print("array before deleting an element")
print(arr1)
print("array after deleting an element")
arr1.remove(1)
print(arr1)

# Time Complexity : O(n)
# Space Complexity : O(1)
