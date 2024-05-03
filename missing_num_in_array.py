arr=list(map(int,input().split()))
n=max(arr)
arr2=[]
for i in range(1,n+1):
    arr2.append(i)

print(arr2)

y=set(arr2).difference(arr)
print(y)