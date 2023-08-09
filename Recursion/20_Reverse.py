# Reverse Solution


def reverse(striing):
    if len(striing) <= 1:
        return striing
    return striing[len(striing) - 1] + reverse(striing[0 : len(striing) - 1])


print(reverse("kamlesh"))
print(reverse("kannya"))
