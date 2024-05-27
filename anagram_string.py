s1 = str(input())
s2  = str(input())
new=[]
for i in s1:
    new.append(i)
     
fg = []
for j in s2:
    fg.append(j)
new.sort()
fg.sort()
if(new==fg):
    print(True)
else:
    print(False)