# Some Recursive Solution


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


print(someRecursive([1, 2, 4, 3, 5, 6], isOdd))
print(someRecursive([2, 4, 6, 9], isOdd))
print(someRecursive([2, 4, 6, 8], isOdd))
