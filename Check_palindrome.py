"""
Problem statement
Check whether a given number ’n’ is a palindrome number.

Note :
Palindrome numbers are the numbers that don't change when reversed.
You don’t need to print anything. Just implement the given function.
Example:
Input: 'n' = 51415
Output: true
Explanation: On reversing, 51415 gives 51415.
"""
n = int(input("Enter the palindrome number:"))


def reverse(n):
    y = str(n)[::-1]
    return y

o = int(reverse(n))
bool = False
def good(bool):
 if(n == o):
    return True
 else:
    return False
print("Palindrome of given number will be:" + str(good(bool)))


##By coding ninja 
"""
n = input()

 

def checkPalindrome(n):

    if n == n[::-1]: # using slicing with negative indexing for reversing the string

        return 'true'

    else:

        return 'false'

print(checkPalindrome(n))

"""