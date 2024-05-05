arr=list(map(int,input().split()))

def sfa(arr):
 n=len(arr)
 if n==1:
  return arr[0]
 
 for i in range(len(arr)):
  if(i==0):
   if(arr[i]!=arr[i+1]):
    return arr[i]
  elif(i==n-1):
    if(arr[i]!=arr[i-1]):
     return arr[i]
  else:
   if(arr[i]!=arr[i+1]) and (arr[i]!=arr[i-1]):
    return arr[i]
 return -1
fs = sfa(arr)

print(fs)

    