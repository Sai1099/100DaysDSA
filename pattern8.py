n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(i-1,n):
        print("*",end=" ")
    print()