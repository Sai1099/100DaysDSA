def cumulative_sum_minus_first(arr):
    # Calculate the cumulative sum
    cumulative = [0]  # Start with zero
    total = 0  # Variable to store the running total
    for num in arr:
        total += num  # Add each element to the total
        cumulative.append(total)  # Store the running total in the list
    
    # Return the list minus the first element (which is the initial 0)
    return cumulative[:-1]


# Input array
input_array = [1, 2, 3, 4, 5]

# Calculate the cumulative sums with the specified adjustment
output_array = cumulative_sum_minus_first(input_array)

print("Output array:", output_array)
