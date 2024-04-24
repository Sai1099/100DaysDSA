pages = int(input())
arr = list(map(int,input().split()))

t =sorted(arr)

y=max(t)
u=min(t)
r=y+u

if(pages == r):
    print(True)
else:
    print(False)