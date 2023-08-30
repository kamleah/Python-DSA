# Initialize an empty list to store numbers
mylist = list()

# Prompt the user to enter numbers and store them in the list
while True:
    inp = input("Enter a number (type 'done' to finish): ")

    # Check if the user wants to stop entering numbers
    if inp == "done":
        break

    # Convert the input to a floating-point number
    value = float(inp)

    # Append the converted value to the list
    mylist.append(value)

# Calculate the average of the numbers in the list
average = sum(mylist) / len(mylist)

# Print the calculated average
print("Average:", float(average))
