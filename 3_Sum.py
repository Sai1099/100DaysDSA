arr = list(map(int,input().split()))

def sum_by_3(arr):
    current_sum =0
    st=set()
    
    for i in range(0,len(arr)):
       for j in range(i+1,len(arr)):
           for k in range(j+1,len(arr)):
               if(arr[i]+arr[j]+arr[k]==0):
                  temp = [arr[i],arr[j],arr[k]]
                  temp.sort()
                  st.add(tuple(temp))
    return st

print(sum_by_3(arr))