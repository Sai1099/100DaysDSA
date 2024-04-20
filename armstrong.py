"""

You are given an integer 'n'. Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.


An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal
to the number itself. For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.
"""

n = input()

y = len(str(n))
count = 0

for i in n:
    math = pow(int(i),int(y))
    count = math + count
    print(math)
print(count)
q = str(count)
if(q==n):
    print("true")
else:
    print("False")