n=int(input())
m=int(input())
def ffasg(n,m):
    for i in range(m):
        y=pow(n,i)
        if(y==m):
            return i
    else:
        return -1