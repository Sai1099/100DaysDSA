arr = list(map(int,input))

def swayam_happy(arr):
    n=len(arr)
    for i in range(len(arr)):
        if(i==0 or arr[i]<arr[i-1] and i==n-1 or arr[i]>arr[i+1]):
            return i