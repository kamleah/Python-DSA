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


list1 = [1, 3, 4, 2, 5]
list2 = [2, 4, 3, 5, 1]

print(permutation(list1=list1, list2=list2))
