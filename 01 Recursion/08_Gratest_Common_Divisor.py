# How to find Gratest Common Divisor of two numbers using recursion.
# Step 1 : Recursive Case - The Flow

# GCD is the largest positive integer that divides the numbers without a remainder

# gcd(8, 12) = 4
# 8 = 2 * 2 * 2
# 12 = 2 * 2 * 3

# Here 2 * 2 is common
# Therefore 2 * 2 = 4 is the GCD

# Euclidean Algorithm
# gcd(48, 18)
# Step 1 : 48/18 = 2 remainder 12
# Step 2 : 18/12 = 1 remainder 6
# Step 3 : 12/6 = 2 remainder 0

# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)


# --------- CODE ---------


def gcd(a, b):
    assert int(a) == a and int(b) == b, "The number must be positive integer only"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(-48, 9))
