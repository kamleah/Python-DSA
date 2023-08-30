# Title: Examples of Converting Strings to Lists and Splitting Strings

# Example 1: Converting a string to a list of characters
a = "string"
print("Example 1:")
print("Original String:", a)
a_list = list(a)
print("Converted List:", a_list)
print()

# Example 2: Splitting a string using whitespace as a delimiter
b = "span span span"
print("Example 2:")
print("Original String:", b)
b_list = b.split()
print("Split List:", b_list)
print()

# Example 3: Splitting a string using a custom delimiter
c = "list-and-string"
delimiter = "-"
print("Example 3:")
print("Original String:", c)
c_list = c.split(delimiter)
print("Split List:", c_list)
print()

# Example 4: Splitting a string using a delimiter and then joining it back
d = "spam-spam1-spam2"
delimiter = "a"
print("Example 4:")
print("Original String:", d)
d_list = d.split(delimiter)
print("Split List:", d_list)
new_string = delimiter.join(d_list)
print("Joined String:", new_string)
