arr = list(map(int,input().split()))
target = int(input())
def floor(arr,target):
    n=len(arr)
    low = 0
    high =n-1
    count=0
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid]==target):
            count+=1
            low = mid+1
        else:
            high = mid-1
    return count

def celi(arr,target):
    n=len(arr)
    low = 0
    high =n-1
    ans = -1
    count=0
    while(low<=high):
        mid = (low+high) // 2
        if(arr[mid]==target):
            count+=1
            high = mid-1
        else:
            low = mid+1
    return count

y=floor(arr,target)
p=celi(arr,target)
z=y+p
print(z)