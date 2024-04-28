A= list(map(int,input().split()))

def permutation(arr):
    # Find the length of the input list
    n = len(A)
    
    # Find the index 'i' such that A[i] is the last element
    # where A[i] is less than the element next to it
    i = n - 2
    while i >= 0 and A[i] >= A[i+1]:
        i -= 1

    # If no such 'i' is found, the list is already in the highest possible order
    # So, reverse the list and return
    if i == -1:
        return A[::-1]
    
    # Find the index 'j' such that A[j] is the smallest element to the right of A[i]
    # and greater than A[i]
    for j in range(n-1, i, -1):
        if A[j] > A[i]:
            # Swap the elements at indices 'i' and 'j'
            A[j], A[i] = A[i], A[j]
            break

    # Reverse the elements from index 'i+1' to the end of the list
    A[i+1:] = reversed(A[i+1:])
    
    # Return the lexicographically next greater permutation
    return A