# is Palindrome Solution


def isPalindrome(striing):
    if len(striing) == 0:
        return True
    if striing[0] != striing[len(striing) - 1]:
        return False
    return isPalindrome(striing[1:-1])


print(isPalindrome("kamlesh"))
print(isPalindrome("kannya"))
print(isPalindrome("nitin"))
