def sumofdigits(n):
    print("------------------------")
    print("value of n---", n)
    if n == 0:
        return 0
    else:
        print("value of result---", int(n % 10))
        print("value of remainder---", int(n / 10))
        return int(n % 10) + sumofdigits(int(n / 10))


print(sumofdigits(129999))
