arr = list(map(int,input().split()))
count=0

for i in range(0,len(arr)):
    max_arr=i
    count=count+arr[i]
    if(max_arr<count):
        max_arr=count

    elif(count<0):
        count=0
print(count)


"""
def GFG(a, size):
    max_so_far = float('-inf')  
    # Use float('-inf') instead of maxint
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
    """