arr = list(map(int,input().split()))

y = arr[0]
print(y)
arr.pop(0)
print(arr)
arr.append(y)
print(arr)