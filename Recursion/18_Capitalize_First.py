# Capitalize First


def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(["kamlesh", "shubhnarayan", "gupta"]))
print(capitalizeFirst(["kannya", "rajendra", "bhoir"]))
