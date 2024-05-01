arr= list(map(int,input().split()))
r=[]
def array(arr):
  for i in range(len(arr)):
     visited = True
     for j in range(i+1,len(arr)):
        if(arr[j]>arr[i]):
            visited = False
            break
     if visited:
       r.append(arr[i])
  return r

print(array(arr))