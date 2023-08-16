from array import *

arr1 = array("i", [1, 2, 3, 4, 5])

print(arr1)


def searchInArray(array, value):
    for i in array:  # --------------------------------------------------- O(n)
        if i == value:  # ------------------------------------------------ O(1)
            return f"index of {value} is {array.index(value)}"  # -------- O(1)
    return "The Element does not exists in this elements"  # ------------- O(1)


print(searchInArray(arr1, 4))

# ----------------------------------------------------------------------------------------------------------------
# ------------------------ Time Complexity Of this function is ------------ O(n)
# ------------------------ Space Complexity Of this function is ----------- O(1)
