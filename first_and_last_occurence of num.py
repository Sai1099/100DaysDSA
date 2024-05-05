arr = list(map(int,input().split()))
target = int(input())
"""
def floor(arr,target):
    n=len(arr)
    low = 0
    high =n-1
    count=0
    ans =-1
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid]==target):
            yoy = n - mid
            ans= yoy

            low = mid+1
        else:
            high = mid-1
    return ans
def celi(arr,target):
    n=len(arr)
    low = 0
    high =n-1
    ans = -1
    count=0
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid]==target):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

print(floor(arr,target))

print(celi(arr,target))
"""
def linear_search(arr,target):
    n=len(arr)
    for i in range(n-1,0,-1):
        if(arr[i] == target):
            return i 
        
    for j in range(len(arr)):
        if(arr[j] == target):
            return j
        
print(linear_search(arr,target))