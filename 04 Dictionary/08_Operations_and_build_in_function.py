# Define a dictionary with number translations
mydict = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez",
}

# Check if the value "uno" is present in the dictionary values
value_check = "uno" in mydict.values()
print("Is 'uno' present in values?", value_check)

# Check if the key "uno" is present in the dictionary keys
key_check = "uno" in mydict.keys()
print("Is 'uno' present in keys?", key_check)

# Iterate through the dictionary and print key-value pairs
print("Iterating through the dictionary:")
for key in mydict:
    print(key, mydict[key])

# Define dictionaries for demonstration
newDict = {1: True, 2: True}
newDict2 = {0: False, 1: False}
newDict3 = {0: True, 1: False, 2: True}
newDict4 = {0: True, 1: False, 2: False}
newDict5 = {}

# Use the all() function to check if all values are truthy
print("all(newDict):", all(newDict))  # Output: True
print("all(newDict2):", all(newDict2))  # Output: False
print("all(newDict3):", all(newDict3))  # Output: False
print("all(newDict4):", all(newDict4))  # Output: False
print("all(newDict5):", all(newDict5))  # Output: True (no values to check)

# Calculate the length of the dictionary mydict
dict_length = len(mydict)
print("Length of mydict:", dict_length)

# Define a dictionary with vowel counts
vowelsDict = {"e": 1, "a": 2, "u": 3, "o": 4, "i": 5}

# Sort the keys of vowelsDict and mydict in ascending order
sorted_vowels = sorted(vowelsDict)
sorted_mydict = sorted(mydict)
print("Sorted vowelsDict:", sorted_vowels)
print("Sorted mydict:", sorted_mydict)

# Sort the keys of vowelsDict and mydict in descending order
sorted_vowels_reverse = sorted(vowelsDict, reverse=True)
sorted_mydict_reverse = sorted(mydict, reverse=True)
print("Sorted vowelsDict in reverse:", sorted_vowels_reverse)
print("Sorted mydict in reverse:", sorted_mydict_reverse)

# Sort the keys of mydict based on the length of the keys
sorted_mydict_by_length = sorted(mydict, key=len)
print("Sorted mydict by key length:", sorted_mydict_by_length)

# Sort the keys of lenDict based on the length of the values
lenDict = {"uioi": "oiuyt", "ui": "uyu", "yuiuy": "uiu", "i": "dciu"}
sorted_lenDict_by_value_length = sorted(lenDict, key=len)
print("Sorted lenDict by value length:", sorted_lenDict_by_value_length)
