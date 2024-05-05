arr = list(map(int,input().split()))
target = int(input())
def floor(arr,target):
    n=len(arr)
    low = 0
    high =n-1
    ans = -1
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid]<=target):
            ans= arr[mid]
            low = mid+1
        else:
            high = mid-1
    return ans

def celi(arr,target):
    n=len(arr)
    low = 0
    high =n-1
    ans = -1
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid]>=target):
            ans= arr[mid]
            high = mid-1
        else:
            low = mid+1
    return ans

print(floor(arr,target))
print(celi(arr,target))