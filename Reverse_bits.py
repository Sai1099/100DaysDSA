"""
There is a song concert going to happen in the city. The price of each ticket is equal to the number obtained after reversing the 
bits of a given 32 bits unsigned integer ‘n’.
"""

def change_bin(num):
    binary = bin(num)[2:]
    binary = binary.rjust(32,'0')
    return binary
num = int(input())

d = change_bin(num)
print(change_bin(num))

##we are used slicing to reverse a number
rev = str(d)[::-1]
print(rev)

def change_int(rev):
    return int (rev,2)
print(change_int(rev))


##ALTERNATIVE CODE GIVEN BY CODING NINJA
"""

def reverseBits(i):

    res=0
    c=0
    while i>0:
        res+=(i%2)*2**(31-c)
        i//=2
        c+=1
    return res
    """