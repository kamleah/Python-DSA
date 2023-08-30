# Searching for a value in a dictionary

# Define a dictionary
myDict = {"name": "Kamlesh", "age": 27, "address": "Bhiwandi"}


# Define a function to search for a value in the dictionary
def searchDict(dictionary, value):
    # Iterate through each key in the dictionary
    for key in dictionary:
        # Check if the value of the current key matches the given value
        if dictionary[key] == value:
            # If a match is found, return the key and value
            return key, value
    # If no match is found, return a message indicating the value does not exist
    return "The value does not exist"


# Call the function to search for a value and print the result
result = searchDict(myDict, "Kamlesh")
print(result)
