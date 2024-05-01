arr = list(map(int,input().split()))
n=len(arr)

k=int(input())
def count_array(arr,n):
 count=0
 for i in range(n):
    current_sum=0
    for j in range(i,n):
        current_sum+=arr[j]
        

        if(current_sum == k):
          count+=1

 return count
print(count_array(arr,n))