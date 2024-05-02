arr = list(map(int,input().split()))
def product_array(arr):
    for i in range(len(arr)):
        if(arr[i] == 0):
            y=arr[i]
            arr.pop(i)
    return arr
arr = product_array(arr)
sum=1
for i in range(len(arr)):
     sum=sum*arr[i]

print(sum)
    

   