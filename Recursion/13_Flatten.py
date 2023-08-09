# Flatten Solution


def flatten(arr):
    result = []
    for custItem in arr:
        if type(custItem) is list:
            result.extend(flatten(custItem))
        else:
            result.append(custItem)

    return result


print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, 2, 3, [4, 5, [6], [7], [[8, [9]]]]]))
print(flatten([[[[[[[1]]]]]], [[[[[[[2]]]]]]]]))
