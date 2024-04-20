"""
You are given an integer ‘n’.



Function ‘sumOfDivisors(n)’ is defined as the sum of all divisors of ‘n’.



Find the sum of ‘sumOfDivisors(i)’ for all ‘i’ from 1 to ‘n’.
"""
n = int(input())
total_div=0
for i in range(1,n+1):
    sum_div = 0
    for j in range(1,n+1):
        if(i%j==0):
            sum_div=sum_div+j
    total_div=total_div+sum_div
print(total_div)    