arr = list(map(int,input().split()))

for i in range(len(arr)):
    for i in range(len(arr)):
        if(arr[i]==0):
            y= arr.pop(i)
            arr.append(y)

print(arr)