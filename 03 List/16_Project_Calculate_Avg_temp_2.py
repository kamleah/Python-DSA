# Temperature Analysis and Average Calculation

# Get the number of days from the user
numDays = int(input("How many day's temperature? "))

# Initialize the total temperature variable
total = 0
temps = []  # List to store individual temperatures

# Loop to input temperatures for each day
for i in range(1, numDays + 1):
    nextDay = int(input(f"Day {str(i)}'s high temp:"))
    temps.append(nextDay)  # Store the temperature in the list
    total += nextDay  # Add the temperature to the total

# Calculate the average temperature
avg = round(total / numDays, 2)

# Display the calculated average temperature
print(f"\nAverage = {str(avg)}")

# Count the number of days where temperature is above average
above = 0
for temp in temps:
    if temp > avg:
        above += 1

# Display the count of days with temperature above average
print(f"No of day's temp is above the average: {above}")
