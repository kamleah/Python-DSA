import numpy as np

# Create a NumPy array
myarray = np.array([1, 12, 2, 4, 6, 7, 8, 9, 17])


# Function to find the maximum product of pairs in an array
def findMaxProduct(array):
    maxproduct = 0
    pairs = ""  # Initialize a string to store the pair with maximum product

    # Loop through each element in the array
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # Calculate the product of the current pair
            product = array[i] * array[j]

            # Update the maximum product and the pair if the current product is greater
            if product > maxproduct:
                maxproduct = product
                pairs = f"{array[i]} {array[j]}"

    # Print the pair with the maximum product and the maximum product itself
    print(f"Pair with maximum product: {pairs}")
    print(f"Maximum product: {maxproduct}")


# Call the function to find the maximum product of pairs in the array
findMaxProduct(myarray)
