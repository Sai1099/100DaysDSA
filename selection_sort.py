##n = input()
arr = list(map(int,input().split()))
t = len(arr)

for i in range(t):
    min_pos=i
    for j in range(i,t):
        if(arr[j]<arr[min_pos]):
            min_pos=j

    temp=arr[i]
    arr[i]=arr[min_pos]
    arr[min_pos]=temp
    print(arr)