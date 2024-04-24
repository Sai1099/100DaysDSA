arr = list(map(int,input().split()))

count=0
temp=0
index=0
for i in range(0,len(arr)):
    temp=arr.count(arr[i])
    if(temp>count):
        count=temp
        index=i

print(arr[index])
print(count)
