import math
arr = list(map(int,input().split()))
x_val=int(input())
def iphone(arr,x_val):
    
    maxi= max(arr)
    for d in range(1,maxi+1):
        sum=0
        for j in range(len(arr)):
            sum+=math.ceil(arr[j] / d)
        if(sum<=x_val):
         return d
    return -1
    
print(iphone(arr,x_val))