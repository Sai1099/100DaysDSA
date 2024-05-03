arr=list(map(int,input().split()))
for i in range(len(arr)-1):
    ##print(i)
    for j in range(i+1,len(arr)-1):
        #print(j)
        for k in range(i,j+1):
            print(k)