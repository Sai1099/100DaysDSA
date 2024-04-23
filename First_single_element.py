arr = list(map(int,input().split()))
count =0 
index = 0
temp=0
for i in range(len(arr)):
    temp = arr.count(arr[i])
    if(count<temp):
        count=temp
        index = i
    elif(temp==1):
      print("the single element "+str(arr[i]))


     
