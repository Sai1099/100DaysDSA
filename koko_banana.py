import math
a=list(map(int,input().split()))
t=int(input())
def maxtu(a):
    n=len(a)
    for i in range(n):
        maxi=max(maxi,a[i])
    return maxi

def calculatehour(a,hourly):
    totalH=0
    n=len(a)
    for i in range(n):
      totalH+=math.ceil(a[i] / hourly)
    return totalH

def calculateminimum(a):
    n=len(a)
    low = 0
    high = maxtu(a)
    while low<=high:
      mid=(low+high) // 2
      toatlH=calculatehour(a,mid)
      if toatlH<=t:
           high = mid-1
      else:
         low=mid+1
    return low