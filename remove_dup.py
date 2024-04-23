arr = list(map(int,input().split()))
swat=[]
for i in arr:
    if i not in swat:
       swat.append(i) 

print(swat)
