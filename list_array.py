n=int(input())

t=list(input())
##to know the list size using len
if(n==len(t)):
  print(t)
else:
  print("enter the arrays correctly")

y = sorted(t)

print(y[::-1])
##[::-1] reverse the array or list


"""
from typing import *

 

def reverseArray(n: int, nums: List[int]) -> List[int]:

    def rec(ind, nums):

        if ind == len(nums):

            return []

        res = rec(ind+1, nums)

        res.append(nums[ind])

        return res

 

    res = rec(0, nums)

    return res"""