n1 = int(input())
n2= int(input())
list1=[]
for i in range(1,n1):
    if(n1%i==0):
     list1.append(i)
print(list1)
list4 =[]
for t in range(1,n2):
    if(n2%t==0):
     list4.append(t)
print(list4)
y =list(set(list1).intersection(list4))
print(max(y))
##Coding Ninja code
"""
def calcGDC(a:int, b: int) -> int:

    while(a>0 and b>0):

        if(a>b):

            a=int(a%b)

        else:

            b=int(b%a)

        

    if(a==0):

        return b

    return a

"""