arr = list(map(int,input().split()))
m= int(input())
n=int(input())
def blomming(arr,m,n):
  total=m*n
  t=len(arr)
  if(total>t):
    return -1
  arr.sort()
  print(arr)
  for i in range(t):
    if(i==total-1):
      return arr[i]
"""
 
  low = 0 
  high = t-1
  arr.sort()
  while(low<=high):
    mid=(low+high) / 2
    if(mid == total-1):
      
      high=mid-1
      return arr[mid]
    else:
      low=mid+1
"""  
print(blomming(arr,m,n))