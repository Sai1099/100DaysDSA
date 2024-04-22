arr = list(map(int,input().split()))
def quick_sort(arr):
  if len(arr) <= 1:
        return arr
  pivot = arr[0]
  left= [x for x in arr[1:] if x < pivot]
  mid = [x for x in arr if x == pivot]
  right =[x for x in arr[1:] if x > pivot ]
  return quick_sort(left) + mid + quick_sort(right)

print(quick_sort(arr))