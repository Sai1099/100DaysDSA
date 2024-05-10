arr= list(map(int,input().split()))
stu = int(input())

def calculate_students(arr,stu):
    pages=0
    st=1
    for i in range(len(arr)):
        if(pages +arr[i]<=pages):
            pages +=arr[i]
        else:
            st+=1
            pages=arr[i]
    return st

def fasfsd(arr,stu):
    if(len(arr)<stu):
        return -1
    low = max(arr)
    high = sum(arr)
    for pages in range(low,high+1):
        if calculate_students(arr,stu,pages):
            return pages
    return low