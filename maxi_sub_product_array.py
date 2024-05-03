arr = list(map(int,input().split()))
def maxi_sub_product(arr):
    maxi=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)-1):
            sum = 1
            for k in range(i,j+1):
                sum*=arr[k]
                maxi = max(maxi,sum)
    return maxi
print(maxi_sub_product(arr))