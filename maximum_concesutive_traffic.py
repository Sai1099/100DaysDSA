arr = list(map(int,input().split()))
M = int(input())
count = 0
replacements = 0
for i in range(len(arr)):
    if arr[i] == 0 and replacements<M:
        arr[i] = 1
        replacements = replacements+1

for i in range(len(arr)):
    if(arr[i]==1):
        count+=1

print(count)