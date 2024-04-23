n = int(input())
arr = list(map(int,input().split()))

y=[1,2,3,4,5,6,7,8,9]
for i in range(n):
    if i in y and len(arr)!=n:
     print(i)
   

