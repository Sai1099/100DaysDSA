from typing import *

def compareIfElse(a: int, b: int):
    # Write your code here
    if a > b:
        return "greater"
    elif b > a:
        return "smaller"
    else:
        return "equal"



a,b=map(int,input().split())
# Provide values for a and b
##input_str = input().split()
##a = int(input_str[0])
##b = int(input_str[2])

# Call the function
result = compareIfElse(a, b)
print(result)