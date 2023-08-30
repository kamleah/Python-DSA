# Tuple Operations and Functions

# Defining tuples
mytuple = (1, 4, 3, 2, 5)
mytuple2 = (1, 2, 6, 9, 8, 7, 1)

# Concatenating tuples
combinedtuple = mytuple + mytuple2
print("Concatenated Tuple:", combinedtuple)

# Replicating elements in a tuple
replicated_tuple = mytuple * 4
print("Replicated Tuple:", replicated_tuple)

# Checking for membership
is_present = 4 in mytuple
is_absent = 40 in mytuple
print("Is 4 present?", is_present)  # Output: True
print("Is 40 present?", is_absent)  # Output: False

# Counting occurrences of an element
count_1_in_mytuple = mytuple.count(1)
count_1_in_mytuple2 = mytuple2.count(1)
print("Count of 1 in mytuple:", count_1_in_mytuple)  # Output: 1
print("Count of 1 in mytuple2:", count_1_in_mytuple2)  # Output: 2

# Finding the index of an element
index_of_1_in_mytuple = mytuple.index(1)
index_of_9_in_mytuple2 = mytuple2.index(9)
print("Index of 1 in mytuple:", index_of_1_in_mytuple)  # Output: 0
print("Index of 9 in mytuple2:", index_of_9_in_mytuple2)  # Output: 3

# Getting the length of tuples
length_of_mytuple = len(mytuple)
length_of_mytuple2 = len(mytuple2)
print("Length of mytuple:", length_of_mytuple)  # Output: 5
print("Length of mytuple2:", length_of_mytuple2)  # Output: 7

# Finding minimum and maximum elements
min_of_mytuple = min(mytuple)
min_of_mytuple2 = min(mytuple2)
max_of_mytuple = max(mytuple)
max_of_mytuple2 = max(mytuple2)
print("Min of mytuple:", min_of_mytuple)  # Output: 1
print("Min of mytuple2:", min_of_mytuple2)  # Output: 1
print("Max of mytuple:", max_of_mytuple)  # Output: 5
print("Max of mytuple2:", max_of_mytuple2)  # Output: 9

# Converting a list to a tuple
list_to_tuple = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print("Tuple from List:", list_to_tuple)
