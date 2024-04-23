arr = list(map(int,input().split()))
 
y=sorted(arr)
if(arr == y):
    print(True)
else:
    print(False)