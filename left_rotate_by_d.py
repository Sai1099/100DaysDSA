arr = list(map(int,input().split()))
rotate= int(input())
for i in range(rotate):
    
    y=arr.pop(i)##del(1)
    arr.append(y)##last-1

print(arr)