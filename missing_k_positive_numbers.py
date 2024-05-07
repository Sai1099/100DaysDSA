arr= list(map(int,input().split()))
x =int(input())
def fsdf(arr,x):
    n=len(arr)
    for i in range(n):
        if(arr[i]<=x):
            x+=1
            break
        else:
            break
    return x
   
print(fsdf(arr,x))

