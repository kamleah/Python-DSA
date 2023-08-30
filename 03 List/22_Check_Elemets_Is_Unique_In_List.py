myList = [
    1,
    20,
    30,
    40,
    44,
    5,
    56,
    57,
    8,
    9,
    0,
    19,
    10,
    10,
    10,
    20,
    56,
    57,
]

myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def checkUniqueElements(array):
    uniqueList = []
    for arr in array:
        if arr in uniqueList:
            print(arr)
            return False
        else:
            uniqueList.append(arr)
    return True


print(checkUniqueElements(array=myList))
print(checkUniqueElements(array=myArray))
