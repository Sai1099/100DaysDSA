arr = list(map(int,input().split()))
target = int(input())
def binary(arr,target):
    n=len(arr)
    low=0
    high = n-1
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid] == target):
            return arr
        elif(low>target):
            low = mid+1
        else:
            high = mid-1
    return -1
print(binary(arr,target))