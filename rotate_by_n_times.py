arr = list(map(int,input().split()))
x = int(input())
def swayam(arr,x):
    
    count=0
    for i in range(len(arr)):
        if(arr[i]==x):
            break
        else:
            count=count+1
    else:
        return -1