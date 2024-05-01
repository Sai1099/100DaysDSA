rows = int(input())
columns = int(input())
matrix = []

for i in range(rows):
    r=[]
    for j in range(columns):
        r.append(int(input()))
    matrix.append(r)
n= len(matrix)

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    print()


for i in range(columns):
   matrix[i].reverse()

for i in range (rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()