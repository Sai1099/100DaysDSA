arr = list(map(int,input().split()))

n= len(arr)
def sort(arr):
 for i in range(len(arr)-1,0,-1):
     for j in range(i):
         if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1] = temp
    
sort(arr)
print(arr)


##other
def sort_1(arr):
  sorted = False
  while not sorted:
    sorted = True
    for i in range(0,len(arr)-1):
      if(arr[i]>arr[i+1]):
       sorted = False
       arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
  
print(sort_1(arr))