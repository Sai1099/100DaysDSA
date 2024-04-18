"""
#Problem statement
You are given a number ’n’.



Find the number of digits of ‘n’ that evenly divide ‘n’.



Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.


Example:
Input: ‘n’ = 336

Output: 3

Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.
"""




n = int(input("Enter the n number:"))
digit_count = str(n)
count=0
for digits in digit_count:
    digit = int(digits)
    if(digit!=0 and n%digit==0):
        count+=1
print(count)





