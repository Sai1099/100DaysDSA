arr = list(map(int,input().split()))
negative_int = []
positive_int=[]
y= sorted(arr)
for i in range(len(arr)):
    if(arr[i]<0):
     negative_int.append(arr[i])
    else:
       positive_int.append(arr[i])

print(negative_int)
print(positive_int)
