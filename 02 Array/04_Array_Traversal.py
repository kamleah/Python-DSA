from array import *

arr1 = array("i", [1, 2, 3, 4, 5])

print(arr1)


def traversalArray(arr):
    for i in arr:  # -------------- O(n)
        print(i)  # --------------- O(1)


traversalArray(arr=arr1)

# Time Complexity : O(n)
# Space Complexity : O(1)
