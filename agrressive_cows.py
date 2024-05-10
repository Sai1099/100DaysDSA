def canPlaceCows(stalls, distance, cows):
    # Check if it's possible to place 'cows' with at least 'distance' between them
    n = len(stalls)
    count = 1  # Place the first cow at the first stall
    last_position = stalls[0]

    for i in range(1, n):
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]
            if count == cows:  # If we've placed all cows, return True
                return True
    return False

def aggressiveCows(stalls, k):
    stalls.sort()  # Sort the stalls to make distance calculations easier

    # Binary search for the maximum minimum distance
    left = 1
    right = stalls[-1] - stalls[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if canPlaceCows(stalls, mid, k):
            result = mid  # Update the result to the current distance
            left = mid + 1  # Try for a larger minimum distance
        else:
            right = mid - 1  # Try for a smaller minimum distance

    return result  # This will be the maximum possible minimum distance

# Example usage
stalls = [0, 3, 4, 7, 9, 10]
k = 4
max_min_distance = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", max_min_distance)
