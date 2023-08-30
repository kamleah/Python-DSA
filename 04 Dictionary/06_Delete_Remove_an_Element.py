# Deleting or removing elements from a dictionary

# Define a dictionary
myDict = {
    "name": "Kamlesh",
    "lastname": "Gupta",
    "address": "Bhiwandi",
    "education": "master",
    "age": "27",
    "city": "Bhiwandi",
    "state": "Maharashtra",
}

# Demonstrate the pop() method
# Remove the "name" key and print its value
removed_name = myDict.pop("name")
print("Removed Name:", removed_name)
print("Updated Dictionary:", myDict)

# Demonstrate the popitem() method
# Remove and print the last key-value pair from the dictionary
removed_item = myDict.popitem()
print("Removed Item:", removed_item)
print("Updated Dictionary:", myDict)

# Remove and print another key-value pair using popitem()
removed_item = myDict.popitem()
print("Removed Item:", removed_item)
print("Updated Dictionary:", myDict)

# Demonstrate the del statement
# Remove the "age" key and its value
del myDict["age"]
print("Updated Dictionary:", myDict)

# Demonstrate the clear() method
# Remove all elements from the dictionary
myDict.clear()
print("Cleared Dictionary:", myDict)
