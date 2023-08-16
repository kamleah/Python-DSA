from array import *

arr1 = array("i", [1, 2, 3, 4, 5])

print(arr1)


def accessElement(array, index):
    if index >= len(array):  # -----------------------------------> O(1)
        print("There is not any element in this index")  # -------> O(1)
    else:
        print(array[index])  # -----------------------------------> O(1)
        # -------------------------------------------------------------------------
        # ----------Total Time Complexity -------------------------> O(1)


print(accessElement(array=arr1, index=5))

# Time Complexity : O(1)
# Space Complexity : O(1)
