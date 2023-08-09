# Capitalize Words Solution


def capitalizeWord(arrr):
    result = []
    if len(arrr) == 0:
        return result
    result.append(arrr[0].upper())
    return result + capitalizeWord(arrr[1:])


words = ["i", "am", "kamlesh", "shubhnarayan", "gupta"]
print(capitalizeWord(words))
