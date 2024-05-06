arr = list(map(int,input().split()))
def swayam(arr):
    y = max(arr)
    count=0
    for i in range(len(arr)):
        if(arr[i]==y):
            break
        else:
            count=count+1
    else:
        return -1