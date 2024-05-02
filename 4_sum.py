arr = list(map(int,input().split()))
target = int(input())
def four_sum(arr,target):
 sum=[]
 temp = set()
 for i in range(len(arr)):
      for j in range(i+1,len(arr)):
         for k in range(j+1,len(arr)):
            for l in range(k+1,len(arr)):
               if(arr[i]+arr[j]+arr[k]+arr[l] == target):
                  sum=[arr[i],arr[j],arr[k],arr[l]]
                  sum.sort()
            temp.add(tuple(sum))
 return temp


print(four_sum(arr,target))



