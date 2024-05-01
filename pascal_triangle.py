n=int(input())
def nCr(n,r):
    res = 1
    for i in range(r):
       res = res * (n-i)
       res =res // (i+1)

    return int(res)

def pascal_trianglr(n:int):
 mat=[]
 for rows in range(1,n+1):
     r=[]
     for col in range(1,rows+1):
        r.append(nCr(rows-1,col-1))
     mat.append(r)
 return mat
      
mat=pascal_trianglr(n)
for i in mat:
    for e in i:
        print(e,end =" ")
    print()