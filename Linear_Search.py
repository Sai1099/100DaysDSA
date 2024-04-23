arr = list(map(int,input().split()))
n = int(input())
y = arr.index(n)
print(y)


"""
Alternative code 
    if num not in arr:

            return -1

    for i in range(n):

        if num == arr[i]:

            return i
"""