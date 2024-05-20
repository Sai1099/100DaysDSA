rows = int(input())
columns = int(input())


matrix = []
for i in range(rows):
    r=[]
    for j in range(columns):
        r.append(int(input()))
    matrix.append(r)

sum=0
for i in range(rows):
    for j in range(columns):
      sum = sum+matrix[i][j]
print(sum)
t=rows*columns
y=sum / t
print(y)