j=list(map(int,input().split()))
count=0
index=0
temp=0
for i in range(0,len(j)):
    temp=j.count(j[i])
    
    if(temp>count):
        count=temp
        index=i


print("the max repeat num will be"+ str(j[index]))
print("the times repeated will be"+str(count))



