arr = list(map(int,input().split()))
target = int(input())
"""
def search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        arr.append(target)
        arr.sort()
        return arr
    
print(search(arr,target))
"""

def searchInsert(arr,target):
    n = len(arr)  # size of the array
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= target:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans
print(searchInsert(arr,target))