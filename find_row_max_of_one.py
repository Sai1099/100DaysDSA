rows=int(input())
columns = int(input())
matrix=[]
for i in range(rows):
    r=[]
    for j in range(columns):
        r.append(int(input()))
    matrix.append(r)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end =" ")
    print()

def rowWithMax1s(matrix, rows, columns):
    cnt_max = 0
    index = -1

    # traverse the matrix:
    for i in range(rows):
        cnt_ones = sum(matrix[i])
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index