rows=int(input())
x=int(input())
columns = int(input())
matrix = []
for i in range(rows):
    r=[]
    for j in range(columns):
        r.append(int(input()))
    matrix.append(r)

##print
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end =" ")
    print()


for i in range(rows):
    for j in range(columns):
       if(matrix[i][j] == x):
           print(True)
print(False)
    