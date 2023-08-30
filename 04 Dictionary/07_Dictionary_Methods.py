# Define the original dictionary
myDict = {
    "name": "Kamlesh",
    "lastname": "Gupta",
    "address": "Bhiwandi",
    "education": "master",
    "age": "27",
    "city": "Bhiwandi",
    "state": "Maharashtra",
}

# 1. Using the copy() method to create a shallow copy of the dictionary
copied_dict = myDict.copy()
print("Copied Dictionary:", copied_dict)

# 2. Using the get() method to retrieve the value associated with the key "name"
name = myDict.get("name")
print("Name:", name)

# 3. Using the items() method to retrieve a list of key-value pairs as tuples
items = myDict.items()
print("Items:", items)

# 4. Using the keys() method to retrieve a list of dictionary keys
keys = myDict.keys()
print("Keys:", keys)

# 5. Using the values() method to retrieve a list of dictionary values
values = myDict.values()
print("Values:", values)

# 6. Using the popitem() method to remove and return the last key-value pair
removed_item = myDict.popitem()
print("Removed Item:", removed_item)
print("Updated Dictionary:", myDict)

# 7. Using the setdefault() method to set a default value for a new key
middlename = myDict.setdefault("middlename", "Shubhnarayan")
print("Middle Name:", middlename)
print("Updated Dictionary:", myDict)

# 8. Using the pop() method to remove and return the value associated with the key "middlename"
removed_middlename = myDict.pop("middlename")
print("Removed Middle Name:", removed_middlename)
print("Updated Dictionary:", myDict)

# Create a new dictionary using fromkeys() with specified keys and a default value
newDict = {}.fromkeys([1, 2, 3], 1)
print("New Dictionary:", newDict)

# 9. Using the update() method to update the dictionary with newDict
myDict.update(newDict)
print("Updated Dictionary:", myDict)

# Create a new dictionary using fromkeys() with only keys and no default value
newDict2 = {}.fromkeys([1, 2, 3])
print("New Dictionary with No Default Value:", newDict2)

# 10. Using the clear() method to remove all elements from the dictionary
myDict.clear()
print("Cleared Dictionary:", myDict)
