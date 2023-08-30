# List to search
myList = [10, 20, 30, 40, 50, 60, 70]

# Search for 40 in the list using the 'in' operator and index()
if 40 in myList:
    print(
        "Value 40 found at index:", myList.index(40)
    )  # Time Complexity: O(n) (index())
else:
    print("The value does not exist in the list")


# Search for a value in the list using a function
def searchingList(lst, value):
    for i in lst:  # Iterate through the list
        if i == value:  # Check if the current element matches the value
            return lst.index(value)  # If found, return the index of the value
    return "Value not found"


print(searchingList(myList, 40))  # Time Complexity: O(n), Space Complexity: O(1)
print(searchingList(myList, 100))  # Time Complexity: O(n), Space Complexity: O(1)
