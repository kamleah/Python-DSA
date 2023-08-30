# Initialize variables to store total and count of numbers entered
total = 0
count = 0

# Prompt the user to enter numbers and calculate the average
while True:
    inp = input("Enter a number (type 'done' to finish): ")

    # Check if the user wants to stop entering numbers
    if inp == "done":
        break

    # Convert the input to a floating-point number
    value = float(inp)

    # Update total by adding the new value
    total = total + value

    # Update the count of numbers entered
    count = count + 1

    # Calculate the average based on the current total and count
    average = total / count

# Print the calculated average
print("Average:", average)
