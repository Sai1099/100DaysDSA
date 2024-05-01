rows = int(input())
columns = int(input())
matrix = []
for i in range(rows):
    r=[]
    for j in range(columns):
        r.append(int(input()))
    matrix.append(r)


for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
n=len(matrix)
m=len(matrix[0])
def markrow(matrix,i,m):
    for j in range(m):
        if(matrix[i][j]!=0):
            matrix[i][j] = -1
def markcolum(matrix,j,n):
    for i in range(n):
        if(matrix[i][j]!=0):
            matrix[i][j] = -1


def zero_matrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 0):
                markrow(matrix,i,m)
                markcolum(matrix,i,n)

    for i in range(n):
        for j in range(m):
              if(matrix[i][j]==-1):
                matrix[i][j] = 0

    return matrix



print(zero_matrix(matrix,n,m))