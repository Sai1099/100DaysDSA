arr = list(map(int,input().split()))
def max_price(arr):
  max_price = 0
  min_price = float('inf')
  for i in range(len(arr)):
      min_price = min(min_price,arr[i])
      max_price = max(max_price,arr[i]-min_price)
  return max_price

max_price(arr)
print(max_price(arr))