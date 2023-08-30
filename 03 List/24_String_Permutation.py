# Question - 6 - Permutation


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


list1 = ["a", "c", "b", "d", "f", "e"]
list2 = ["e", "f", "d", "b", "c", "a"]

print(permutation(list1=list1, list2=list2))
