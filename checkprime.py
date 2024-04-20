"""
A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.



You are given a number 'n'.



Find out whether 'n' is prime or not.

"""
n = int(input())
count=0
for i in range(1,n):
 
 if(n%i==0):
  count=count+1
  print(count)
if(count==1):
  print("true")
else:
  print("false")