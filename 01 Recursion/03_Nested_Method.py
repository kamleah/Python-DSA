def firstMethod():
    secondMethod()
    print("I am first Method")


def secondMethod():
    thirdMethod()
    print("I am second Method")


def thirdMethod():
    fourthMethod()
    print("I am third Method")


def fourthMethod():
    print("I am final Method")


firstMethod()
