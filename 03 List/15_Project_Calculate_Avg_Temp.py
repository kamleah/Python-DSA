# Get the number of days from the user
numDays = int(input("How many day's temperature? "))

# Initialize the total temperature variable
total = 0

# Loop to input temperatures for each day
for i in range(1, numDays + 1):
    nextDay = int(input(f"Day {str(i)}'s high temp:"))
    total += nextDay  # Add the temperature to the total

# Calculate the average temperature
avg = round(total / numDays, 2)

# Display the calculated average temperature
print(f"\nAverage = {str(avg)}")
