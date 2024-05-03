arr = list(map(int,input().split()))
n=max(arr)
def count_num(arr):
    count=0
    temp=0
    index=0
    for i in range(len(arr)):
        temp=arr.count(arr[i])
        if(temp>count):
            count=temp
            index = i
    return index

index = count_num(arr)
def missing_num(arr,n):
    yow=[]
    for i in range(1,n+1):
        yow.append(i)


    y=set(yow).difference(arr)
    return y
y = missing_num(arr,n)
print(arr[index])
print(y)