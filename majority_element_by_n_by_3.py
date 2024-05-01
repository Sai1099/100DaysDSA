arr = list(map(int,input().split()))
def count_ele(arr):
    count=0
    index=0
    temp=0
    res=[]
    for i in range(0,len(arr)):
        
        temp = arr.count(arr[i])
        if(count<temp):
            count= temp
            index=i
            ##don't include count
            res = [arr[i]] ## to start with most frequent num

        elif(count==temp) and arr[i] not in res:
            res.append(arr[i])


    return res


print(count_ele(arr))