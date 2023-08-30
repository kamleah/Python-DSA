# Creating a shopping list
shoppingList = ["Milk", "Cheese", "Butter"]

# Using a for loop to traverse the shoppingList
# The `range(len(shoppingList))` generates indices from 0 to (length - 1) of the list
for i in range(len(shoppingList)):
    # Accessing and printing the element at index `i` in the shoppingList
    print("Item at index", i, ":", shoppingList[i])
