# Traversing through a dictionary

# Define a dictionary
myDict = {"name": "Kamlesh", "age": 27, "address": "Bhiwandi"}


# Define a function to traverse the dictionary
def traverseDict(dictionary):
    # Iterate through each key in the dictionary
    for key in dictionary:
        # Print the key and its corresponding value
        print(key, dictionary[key])


# Call the function to traverse and print key-value pairs
traverseDict(myDict)
