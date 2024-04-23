arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

y = set(arr).union(arr2)
print(y)


"""
  arr= list(set(a+b))

      arr.sort()

      return arr
      """