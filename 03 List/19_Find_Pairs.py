# Title: Find Pairs with Given Sum in a List
# Description: This code finds pairs of numbers in a list that sum up to a given target value.


def findPairs(nums, target):
    # Loop through each element in the list
    for i in range(len(nums)):
        # Loop through the remaining elements after index i
        for j in range(i + 1, len(nums)):
            # Check if the two numbers are equal; if yes, continue to the next iteration
            if nums[i] == nums[j]:
                continue
            # Check if the sum of the two numbers is equal to the target
            elif nums[i] + nums[j] == target:
                # Print the indices of the pair that adds up to the target
                print(f"Pair found at indices: ({i}, {j})")


# List of numbers
myList = [1, 2, 3, 2, 3, 4, 5, 6]

# Target sum
target_sum = 4

# Function call to find pairs
findPairs(myList, target_sum)

# Title: Find Unique Pairs with Given Sum in a List
# Description: This code finds unique pairs of numbers in a list that sum up to a given target value.


def findUniquePairs(nums, target):
    # Create a set to store indices of numbers that have been used in pairs
    used_indices = set()

    # Loop through each element in the list
    for i in range(len(nums)):
        # Check if the current index is already used in a pair
        if i in used_indices:
            continue

        # Loop through the remaining elements after index i
        for j in range(i + 1, len(nums)):
            # Check if the current index is already used in a pair
            if j in used_indices:
                continue

            # Check if the sum of the two numbers is equal to the target
            if nums[i] + nums[j] == target:
                # Print the indices of the unique pair that adds up to the target
                print(f"Unique pair found at indices: ({i}, {j})")

                # Mark the used indices
                used_indices.add(i)
                used_indices.add(j)


# List of numbers
myList = [1, 2, 3, 2, 3, 4, 5, 6, 2]

# Target sum
target_sum = 4

# Function call to find unique pairs
findUniquePairs(myList, target_sum)

# Title: Find Unique and Duplicate Pairs with Given Sum in a List
# Description: This code finds unique and duplicate pairs of numbers in a list that sum up to a given target value.


def findPairs2(nums, target):
    # Create sets to store indices of numbers that have been used in pairs
    used_indices = set()
    duplicate_pairs = set()

    # Loop through each element in the list
    for i in range(len(nums)):
        # Check if the current index is already used in a pair
        if i in used_indices:
            continue

        # Loop through the remaining elements after index i
        for j in range(i + 1, len(nums)):
            # Check if the current index is already used in a pair
            if j in used_indices:
                continue

            # Check if the sum of the two numbers is equal to the target
            if nums[i] + nums[j] == target:
                # Check if the pair is a duplicate
                if (nums[i], nums[j]) in duplicate_pairs or (
                    nums[j],
                    nums[i],
                ) in duplicate_pairs:
                    continue

                # Check if the pair is unique
                if nums[i] != nums[j]:
                    print(f"Unique pair found at indices: ({i}, {j})")
                else:
                    print(f"Duplicate pair found at indices: ({i}, {j})")
                    duplicate_pairs.add((nums[i], nums[j]))

                # Mark the used indices
                used_indices.add(i)
                used_indices.add(j)


# List of numbers
myList = [1, 2, 3, 2, 3, 4, 5, 6]

# Target sum
target_sum = 4

# Function call to find pairs
findPairs2(myList, target_sum)
