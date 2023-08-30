import random

# Q-1. What will be the output of the following code block ?
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])

# The output of the following code block will be:

# ```
# [1, 3, 5, 7, 9]
# ```

# Explanation:
# 1. `a = [1, 2, 3, 4, 5, 6, 7, 8, 9]`: This line initializes a list named `a` containing the numbers from 1 to 9.

# 2. `a[::2]`: This line uses slicing to create a sublist of the list `a`. The slicing format is `[start:stop:step]`, where:
#    - `start` is not specified, so it starts from the beginning (index 0).
#    - `stop` is not specified, so it goes up to the end of the list (index 8, inclusive).
#    - `step` is 2, which means every second element is included in the result.

# 3. The result of the slicing operation `a[::2]` is `[1, 3, 5, 7, 9]`, which contains every second element of the original list `a`.

# 4. `print(a[::2])`: This line prints the result of the slicing operation, which is `[1, 3, 5, 7, 9]`.

# Therefore, the code prints the elements at odd indexes in the list `a`, resulting in the output `[1, 3, 5, 7, 9]`.

# Q-2. What will be the output of following code snippet ?
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    a[::2] = 10, 20, 30, 40, 50, 60
    print(a)
except ValueError:
    print("Error: ValueError - Incorrect number of values for assignment")
except TypeError:
    print("Error: TypeError - Cannot assign values of different lengths")
except Exception as e:
    print("An error occurred:", e)

# A. ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# B. [10,2,20,4,30,6,40,8,50,60]
# C. [1,2,10,20,30,40,50,60]
# D. [1, 10, 3, 20, 5, 30, 7, 40, 9, 50, 60]

# O/P : A. ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# With this code, you'll get a SyntaxError because the assignment statement is not using the correct syntax to assign multiple values to a slice.
# To fix this issue, you need to use square brackets [] to create a list for assignment:

# Q-3. What will be the output of the following code snippet ?
a = [1, 2, 3, 4, 5]
print(a[3:0:-1])

# A. Syntax Error
# B. [4, 3, 2]
# C. [4, 3]
# D. [4, 3, 2, 1]

# The output of the following code block will be:

# ```
# [4, 3, 2]
# ```

# Explanation:
# 1. `a = [1, 2, 3, 4, 5]`: This line initializes a list named `a` containing the numbers from 1 to 5.

# 2. `a[3:0:-1]`: This line uses slicing to create a sublist of the list `a`. The slicing format is `[start:stop:step]`, where:
#    - `start` is 3, which is the index to start slicing from.
#    - `stop` is 0, which is the index to stop slicing at. Note that the stop index is exclusive, so the element at index 0 will not be included.
#    - `step` is -1, which means the slicing goes backward with a step of -1.

# 3. The result of the slicing operation `a[3:0:-1]` is `[4, 3, 2]`, which includes the elements at indexes 3, 2, and 1.

# 4. `print(a[3:0:-1])`: This line prints the result of the slicing operation, which is `[4, 3, 2]`.

# Therefore, the code prints a sublist of elements from the original list `a`, starting from index 3 and moving backward with a step of -1, resulting in the output `[4, 3, 2]`.

# Q-4. What will be the output of the following code snippet ?


def f(value, values):
    v = 1
    values[0] = 44


t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

# A. 1 44
# B. 3 1
# C. 3 44
# D. 1 1

# O/P C. 3 44

# Here's the explanation of the given code:

# 1. `def f(value, values):`: This line defines a function named `f` that takes two parameters: `value` and `values`.

# 2. Inside the function `f`:
#    - `v = 1`: This line initializes a local variable `v` with the value 1. This variable doesn't affect the outside scope because it's local to the function.
#    - `values[0] = 44`: This line modifies the value at index 0 of the `values` list to 44. Since lists are mutable objects, this change will affect the original list `v` passed to the function.

# 3. `t = 3`: This line initializes a variable `t` with the value 3.

# 4. `v = [1, 2, 3]`: This line initializes a list `v` containing the elements 1, 2, and 3.

# 5. `f(t, v)`: This line calls the function `f` with the values of `t` and `v` as arguments. Inside the function, the value at index 0 of the `values` list (which is `v`) is changed to 44.

# 6. `print(t, v[0])`: This line prints the values of `t` and the first element of list `v`. The first element of list `v` was modified inside the function, so it will be 44.

# Output:
# ```
# 3 44
# ```

# Explanation:
# - The value of `t` (which is 3) is printed first.
# - The first element of the list `v` was modified inside the function to be 44, so the output will also be 44.

# The code demonstrates the concept of passing mutable objects (like lists) to functions, where changes made to the object within the function are reflected outside the function as well.

# Q-5. What is the correct command to shuffle the following list ?
fruit = ["apple", "banana", "papaya", "cherry", "mango"]
# A. fruit.shuffle()
# B. shuffle(fruit)
# C. random.shuffle(fruit)
# D. random.shuffleList(fruit)

random.shuffle(fruit)
print(fruit)

# O/P : C. random.shuffle(fruit)

# Q-6. What will be the output of the following code snippet ?

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element

    return v


print(f"Output of question 6 is {fun(data[0])}\n")

# A. 1
# B. 2
# C. 3
# D. 4
# E. 5
# F. 6

# O/P 4, Ans: D.

arr = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

for i in range(0, 4):
    popped_value = arr[i].pop()
    print(f"Removed value: {popped_value}")
    print(f"Modified list: {arr}")

# A. 1 2 3 4
# B. 1 4 8 12
# C. 4 7 11 15
# D. 12 13 14 15

# O/P 4 7 11 15 ANS is C.

# Q-8 What will be the output of the following code snippet ?

print()


def f(i, values=[]):
    values.append(i)
    print(values)
    return values


f(1)
f(2)
f(3)

# A. [1] [2] [3]
# B. [1,2,3]
# C. [1], [1, 2], [1, 2, 3]
# D. 1 2 3

# O/P is [1], [1, 2], [1, 2, 3], ans is C.

# Q-9. What will be the output of the following code snippet?

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end=" ")
# A. 1 2 3 4 5 6
# B. 2 3 4 5 6 1
# C. 1 1 2 3 4 5
# D. 2 3 4 5 6 6

# O/P 2 3 4 5 6 6 ans is D.


# Q-10. What will be the output of the following code snippet?

fruit_list1 = ["Apple", "Berry", "Cherry", "Papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = "Guava"
fruit_list3[1] = "Kiwi"

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == "Guava":
        sum += 1
    if ls[1] == "Kiwi":
        sum += 20

print(sum)
# A. 22
# B. 21
# C. 0
# D. 43

# O/P is 22 ans is A.
