"""
You are given an integer ‘n’.



Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.
"""
n = int(input())
y = list(range(1,n+1))
print(y)
y.reverse()
print(y)
