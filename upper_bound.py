arr = list(map(int,input().split()))
target = int(input())
def sagas(arr,target):
 n=len(arr)
 for i in range(n):
    if(arr[i]<target):
        return i
 return n
print(sagas(arr,target))