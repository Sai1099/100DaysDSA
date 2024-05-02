arr = list(map(int,input().split()))
target = int(input())
def largest(arr,target):
    maxi=0
    
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if(sum == target):
                maxi = max(maxi,j-i+1)
    return maxi

print(largest(arr,target))