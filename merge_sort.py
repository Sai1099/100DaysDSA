arr = list(map(int,input().split()))
def merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left = merge_Sort(left_half)
    right = merge_Sort(right_half)
    return merge(left,right)

def merge(left,right):
    i=j=0
    result=[]
    if i<len(left) and j<len(right):
        if(left[i]<right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_Sort(arr))

