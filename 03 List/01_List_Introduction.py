# Python List
# A list is a data structure that holds an ordered collection of items
# [Milk, Eggs, Cheese, Buttter]  // there are the elements or items of list
# [10, 20, 30, 40] Integers  List
# ["Kamlesh", "Kannya"] Strings List
# ["Kamlesh", 1,3.0, 5] String, Integer, Float
# ["Kannya", 2, 3.0, [10, 20]] String, Integer, Float, Nested List

# Creating a list of integers
integerList = [1, 2, 3, 4]
print("Integer List:", integerList)

# Creating a list of strings
stringList = ["kamlesh", "kannya"]
print("String List:", stringList)

# Creating a mixed list with integers, float, and a string
mixList = [1, 2, 3.0, "Kamlesh"]
print("Mixed List:", mixList)

# Creating a nested list with integers, floats, and strings
nestedList = [1, 3, 4, 6, [1.4, 4.5], ["Kamlesh", "Kannya"]]
print("Nested List:", nestedList)

# Accessing and printing the first element of each list
first_integer = integerList[0]
print("First Integer:", first_integer)

first_string = stringList[0]
print("First String:", first_string)

first_mix = mixList[0]
print("First Element in Mixed List:", first_mix)

# Accessing and printing the second element of the nested list
second_nested = nestedList[1]
print("Second Element in Nested List:", second_nested)

# Accessing and printing the first element of the nested list within the outer nested list
first_inner_nested = nestedList[4][0]
print("First Element in Inner Nested List:", first_inner_nested)
